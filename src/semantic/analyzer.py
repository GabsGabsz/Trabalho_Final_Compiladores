# pyright: reportOptionalMemberAccess=false
# pyright: reportOptionalIterable=false
# pyright: reportArgumentType=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportAttributeAccessIssue=false

from dataclasses import dataclass

from JSSParserVisitor import JSSParserVisitor

from errors.compiler_error import CompilerError
from semantic.scopes import ScopeStack
from semantic.symbols import Symbol
from semantic.types import (
    JssType,
    INT,
    REAL,
    STR,
    BOOL,
    VOID,
    NULL,
    numeric_result,
    can_assign,
    can_cast,
)


@dataclass
class ExprInfo:
    type: JssType
    symbol: Symbol | None = None
    is_lvalue: bool = False
    is_const: bool = False


class SemanticAnalyzer(JSSParserVisitor):
    def __init__(self):
        super().__init__()
        self.scopes = ScopeStack()
        self.loop_depth = 0
        self.current_function: Symbol | None = None
        self.current_class: Symbol | None = None
        self.known_classes: set[str] = set()

    # ======================================================
    # Utilidades
    # ======================================================

    def analyze(self, tree):
        self.collect_global_declarations(tree)
        self.visit(tree)

        main_symbol = self.scopes.resolve_global("main")
        if main_symbol is not None:
            if main_symbol.kind != "function":
                self.error_from_symbol(main_symbol, "'main' deve ser uma funcao.")
            if len(main_symbol.params) != 0:
                self.error_from_symbol(main_symbol, "funcao 'main' nao pode ter parametros.")

    def error(self, ctx, message: str):
        token = ctx.start
        raise CompilerError(
            phase="SEMANTICO",
            line=token.line,
            column=token.column + 1,
            message=message
        )

    def error_from_symbol(self, symbol: Symbol, message: str):
        raise CompilerError(
            phase="SEMANTICO",
            line=symbol.line,
            column=symbol.column,
            message=message
        )

    def symbol_from_token(self, token, typ: JssType, kind: str, is_const: bool = False) -> Symbol:
        return Symbol(
            name=token.getText(),
            type=typ,
            kind=kind,
            line=token.symbol.line,
            column=token.symbol.column + 1,
            is_const=is_const
        )

    # ======================================================
    # Coleta global: classes e funcoes antes da visita
    # ======================================================

    def collect_global_declarations(self, program_ctx):
        # Primeiro registra classes.
        for top in program_ctx.topLevelDeclaration():
            class_ctx = top.classDeclaration()
            if class_ctx is not None:
                name_token = class_ctx.ID().symbol
                name = class_ctx.ID().getText()

                class_symbol = Symbol(
                    name=name,
                    type=JssType(name),
                    kind="class",
                    line=name_token.line,
                    column=name_token.column + 1,
                )

                self.scopes.global_scope.define(class_symbol)
                self.known_classes.add(name)

        # Depois registra funcoes.
        for top in program_ctx.topLevelDeclaration():
            func_ctx = top.functionDeclaration()
            if func_ctx is not None:
                name_token = func_ctx.ID().symbol
                name = func_ctx.ID().getText()
                return_type = self.type_from_return_type(func_ctx.returnType())
                params = self.params_from_parameter_list(func_ctx.parameterList())

                function_symbol = Symbol(
                    name=name,
                    type=return_type,
                    kind="function",
                    line=name_token.line,
                    column=name_token.column + 1,
                    params=params,
                    return_type=return_type
                )

                self.scopes.global_scope.define(function_symbol)

        # Registra variaveis globais declaradas em sentencas de topo.
        for top in program_ctx.topLevelDeclaration():
            stmt_ctx = top.statement()
            if stmt_ctx is not None and stmt_ctx.variableDeclaration() is not None:
                self.declare_variable_declaration(stmt_ctx.variableDeclaration(), check_initializer=False)

        # Por fim, completa informacoes internas das classes.
        for top in program_ctx.topLevelDeclaration():
            class_ctx = top.classDeclaration()
            if class_ctx is not None:
                self.collect_class_members(class_ctx)

    def collect_class_members(self, class_ctx):
        class_name = class_ctx.ID().getText()
        class_symbol = self.scopes.resolve_global(class_name)

        if class_symbol is None:
            self.error(class_ctx, f"classe '{class_name}' nao encontrada.")

        found_constructor = False
        method_started = False

        for member in class_ctx.classMember():
            field_ctx = member.fieldDeclaration()
            constructor_ctx = member.constructorDeclaration()
            method_ctx = member.methodDeclaration()

            if field_ctx is not None:
                if method_started:
                    self.error(field_ctx, "atributos da classe devem ser declarados antes de metodos.")

                field_name = field_ctx.ID().getText()
                field_type = self.type_from_type_ctx(field_ctx.type_())

                if field_name in class_symbol.fields:
                    self.error(field_ctx, f"atributo '{field_name}' ja declarado na classe '{class_name}'.")

                token = field_ctx.ID().symbol
                class_symbol.fields[field_name] = Symbol(
                    name=field_name,
                    type=field_type,
                    kind="field",
                    line=token.line,
                    column=token.column + 1
                )

            elif constructor_ctx is not None:
                method_started = True
                found_constructor = True

                constructor_class_name = constructor_ctx.ID().getText()
                if constructor_class_name != class_name:
                    self.error(
                        constructor_ctx,
                        f"constructor da classe '{class_name}' nao pode usar o nome '{constructor_class_name}'."
                    )

                class_symbol.constructor_params = self.params_from_parameter_list(
                    constructor_ctx.parameterList()
                )

            elif method_ctx is not None:
                method_started = True
                method_name = method_ctx.ID().getText()
                method_return = self.type_from_return_type(method_ctx.returnType())
                method_params = self.params_from_parameter_list(method_ctx.parameterList())

                if method_name in class_symbol.methods:
                    self.error(method_ctx, f"metodo '{method_name}' ja declarado na classe '{class_name}'.")

                token = method_ctx.ID().symbol
                class_symbol.methods[method_name] = Symbol(
                    name=method_name,
                    type=method_return,
                    kind="method",
                    line=token.line,
                    column=token.column + 1,
                    params=method_params,
                    return_type=method_return
                )

        if not found_constructor:
            self.error(class_ctx, f"classe '{class_name}' deve possuir um constructor.")

    # ======================================================
    # Tipos
    # ======================================================

    def type_from_type_ctx(self, ctx) -> JssType:
        base = ctx.baseType().getText()

        if base not in {"int", "real", "str", "bool"} and base not in self.known_classes:
            self.error(ctx, f"tipo '{base}' nao declarado.")

        array_suffix = ctx.arraySuffix()
        if array_suffix is not None:
            dimensions = tuple(int(tok.getText()) for tok in array_suffix.INT_LITERAL())
            if any(size <= 0 for size in dimensions):
                self.error(ctx, "dimensao do vetor deve ser maior que zero.")
            return JssType(base, is_array=True, array_size=dimensions[0], dimensions=dimensions)

        return JssType(base)

    def type_from_return_type(self, ctx) -> JssType:
        if ctx.VOID() is not None:
            return VOID

        # A especificacao (secao 4.4) proibe retorno de vetor; o proprio
        # tests/prof/6_functions.jss, que declara "function int[5] ...",
        # e um teste negativo e deve falhar aqui.
        return_type = self.type_from_type_ctx(ctx.type_())
        if return_type.is_array:
            self.error(ctx, "funcao ou metodo nao pode retornar vetor.")

        return return_type

    def params_from_parameter_list(self, parameter_list_ctx) -> list[tuple[str, JssType]]:
        params: list[tuple[str, JssType]] = []

        if parameter_list_ctx is None:
            return params

        seen: set[str] = set()

        for param_ctx in parameter_list_ctx.parameter():
            name = param_ctx.ID().getText()
            typ = self.type_from_type_ctx(param_ctx.type_())

            if name in seen:
                self.error(param_ctx, f"parametro '{name}' duplicado.")

            seen.add(name)
            params.append((name, typ))

        return params

    # ======================================================
    # Visitas principais
    # ======================================================

    def visitProgram(self, ctx):
        for top in ctx.topLevelDeclaration():
            self.visit(top)

    def visitTopLevelDeclaration(self, ctx):
        if ctx.statement() is not None:
            self.visit(ctx.statement())
        elif ctx.functionDeclaration() is not None:
            self.visit(ctx.functionDeclaration())
        elif ctx.classDeclaration() is not None:
            self.visit(ctx.classDeclaration())

    def declare_variable_declaration(self, ctx, check_initializer: bool = True):
        modifier = ctx.variableModifier().getText()
        is_const = modifier == "const"
        declared_type = self.type_from_type_ctx(ctx.type_())

        for declarator in ctx.variableDeclarator():
            name_token = declarator.ID().symbol
            name = declarator.ID().getText()

            symbol = Symbol(
                name=name,
                type=declared_type,
                kind="constant" if is_const else "variable",
                line=name_token.line,
                column=name_token.column + 1,
                is_const=is_const
            )

            existing = self.scopes.current_scope.resolve_local(name)
            if existing is None:
                self.scopes.define(symbol)
            elif not (check_initializer and existing.line == symbol.line and existing.column == symbol.column):
                self.scopes.define(symbol)

            if check_initializer:
                initializer = declarator.initializer()

                if is_const and initializer is None:
                    self.error(declarator, f"constante '{name}' deve ser inicializada.")

                if initializer is not None:
                    init_type = self.initializer_type(initializer)

                    if not can_assign(declared_type, init_type, self.known_classes):
                        self.error(
                            initializer,
                            f"nao e possivel atribuir valor do tipo '{init_type}' "
                            f"ao identificador '{name}' do tipo '{declared_type}'."
                        )

    def visitVariableDeclaration(self, ctx):
        self.declare_variable_declaration(ctx, check_initializer=True)

    def initializer_type(self, ctx) -> JssType:
        if ctx.expression() is not None:
            return self.expression_info(ctx.expression()).type

        array_ctx = ctx.arrayLiteral()
        expressions = array_ctx.expression()

        if not expressions:
            return JssType("empty_array", is_array=True, array_size=0, dimensions=(0,))

        first_type = self.expression_info(expressions[0]).type

        for expr in expressions[1:]:
            current_type = self.expression_info(expr).type
            if current_type != first_type:
                self.error(expr, "todos os elementos do vetor devem possuir o mesmo tipo.")

        return JssType(first_type.name, is_array=True, array_size=len(expressions), dimensions=(len(expressions),))

    def visitFunctionDeclaration(self, ctx):
        name = ctx.ID().getText()
        function_symbol = self.scopes.resolve_global(name)

        previous_function = self.current_function
        self.current_function = function_symbol

        self.scopes.enter(f"function:{name}")

        for param_name, param_type in function_symbol.params:
            self.scopes.define(Symbol(
                name=param_name,
                type=param_type,
                kind="parameter",
                line=ctx.start.line,
                column=ctx.start.column + 1
            ))

        self.visit(ctx.block())

        self.scopes.exit()
        self.current_function = previous_function

    def visitClassDeclaration(self, ctx):
        class_name = ctx.ID().getText()
        class_symbol = self.scopes.resolve_global(class_name)

        previous_class = self.current_class
        self.current_class = class_symbol

        for member in ctx.classMember():
            if member.constructorDeclaration() is not None:
                self.visit(member.constructorDeclaration())
            elif member.methodDeclaration() is not None:
                self.visit(member.methodDeclaration())

        self.current_class = previous_class

    def visitConstructorDeclaration(self, ctx):
        class_name = self.current_class.name

        self.scopes.enter(f"constructor:{class_name}")

        self.scopes.define(Symbol(
            name="this",
            type=JssType(class_name),
            kind="this",
            line=ctx.start.line,
            column=ctx.start.column + 1
        ))

        for param_name, param_type in self.current_class.constructor_params:
            self.scopes.define(Symbol(
                name=param_name,
                type=param_type,
                kind="parameter",
                line=ctx.start.line,
                column=ctx.start.column + 1
            ))

        previous_function = self.current_function
        self.current_function = Symbol(
            name=f"{class_name}.constructor",
            type=VOID,
            kind="constructor",
            line=ctx.start.line,
            column=ctx.start.column + 1,
            return_type=VOID
        )

        self.visit(ctx.block())

        self.current_function = previous_function
        self.scopes.exit()

    def visitMethodDeclaration(self, ctx):
        method_name = ctx.ID().getText()
        method_symbol = self.current_class.methods[method_name]

        self.scopes.enter(f"method:{self.current_class.name}.{method_name}")

        self.scopes.define(Symbol(
            name="this",
            type=JssType(self.current_class.name),
            kind="this",
            line=ctx.start.line,
            column=ctx.start.column + 1
        ))

        for param_name, param_type in method_symbol.params:
            self.scopes.define(Symbol(
                name=param_name,
                type=param_type,
                kind="parameter",
                line=ctx.start.line,
                column=ctx.start.column + 1
            ))

        previous_function = self.current_function
        self.current_function = method_symbol

        self.visit(ctx.block())

        self.current_function = previous_function
        self.scopes.exit()

    def visitBlock(self, ctx):
        self.scopes.enter("block")

        for statement in ctx.statement():
            self.visit(statement)

        self.scopes.exit()

    def visitStatement(self, ctx):
        if ctx.block() is not None:
            self.visit(ctx.block())
        elif ctx.variableDeclaration() is not None:
            self.visit(ctx.variableDeclaration())
        elif ctx.ifStatement() is not None:
            self.visit(ctx.ifStatement())
        elif ctx.whileStatement() is not None:
            self.visit(ctx.whileStatement())
        elif ctx.forStatement() is not None:
            self.visit(ctx.forStatement())
        elif ctx.breakStatement() is not None:
            self.visit(ctx.breakStatement())
        elif ctx.returnStatement() is not None:
            self.visit(ctx.returnStatement())
        elif ctx.inputStatement() is not None:
            self.visit(ctx.inputStatement())
        elif ctx.consoleLogStatement() is not None:
            self.visit(ctx.consoleLogStatement())
        elif ctx.expression() is not None:
            self.expression_info(ctx.expression())

    # ======================================================
    # Comandos
    # ======================================================

    def visitIfStatement(self, ctx):
        condition_type = self.expression_info(ctx.expression()).type

        if condition_type != BOOL:
            self.error(ctx.expression(), "condicao do if deve ser do tipo bool.")

        self.visit(ctx.block())

        for else_if in ctx.elseIfBlock():
            self.visit(else_if)

        if ctx.elseBlock() is not None:
            self.visit(ctx.elseBlock())

    def visitElseIfBlock(self, ctx):
        condition_type = self.expression_info(ctx.expression()).type

        if condition_type != BOOL:
            self.error(ctx.expression(), "condicao do else if deve ser do tipo bool.")

        self.visit(ctx.block())

    def visitElseBlock(self, ctx):
        self.visit(ctx.block())

    def visitWhileStatement(self, ctx):
        condition_type = self.expression_info(ctx.expression()).type

        if condition_type != BOOL:
            self.error(ctx.expression(), "condicao do while deve ser do tipo bool.")

        self.loop_depth += 1
        self.visit(ctx.block())
        self.loop_depth -= 1

    def visitForStatement(self, ctx):
        self.scopes.enter("for")

        if ctx.forInit() is not None:
            self.visit(ctx.forInit())

        if ctx.forCondition() is not None:
            condition_ctx = ctx.forCondition().expression()
            condition_type = self.expression_info(condition_ctx).type
            if condition_type != BOOL:
                self.error(condition_ctx, "condicao do for deve ser do tipo bool.")

        if ctx.forUpdate() is not None:
            for update_ctx in ctx.forUpdate().expressionList().expression():
                self.expression_info(update_ctx)

        self.loop_depth += 1
        self.visit(ctx.block())
        self.loop_depth -= 1

        self.scopes.exit()

    def visitForInit(self, ctx):
        if ctx.variableDeclaration() is not None:
            self.visit(ctx.variableDeclaration())
        elif ctx.expressionList() is not None:
            for init_ctx in ctx.expressionList().expression():
                self.expression_info(init_ctx)

    def visitBreakStatement(self, ctx):
        if self.loop_depth == 0:
            self.error(ctx, "comando break so pode ser usado dentro de lacos.")

    def visitReturnStatement(self, ctx):
        if self.current_function is None:
            self.error(ctx, "return so pode ser usado dentro de funcao ou metodo.")

        expected = self.current_function.return_type or VOID

        if ctx.expression() is None:
            if expected != VOID:
                self.error(ctx, f"funcao deve retornar valor do tipo '{expected}'.")
            return

        actual = self.expression_info(ctx.expression()).type

        if expected == VOID:
            self.error(ctx, "funcao void nao deve retornar expressao.")

        if not can_assign(expected, actual, self.known_classes):
            self.error(
                ctx,
                f"tipo de retorno incompativel: esperado '{expected}', encontrado '{actual}'."
            )

    def visitInputStatement(self, ctx):
        args = ctx.inputArgumentList().inputArgument() if ctx.inputArgumentList() is not None else []

        for arg in args:
            info = self.postfix_info(arg.postfixExpression())

            if not info.is_lvalue:
                self.error(arg, "input exige variaveis como argumentos.")

            if info.is_const:
                self.error(arg, "input nao pode alterar constante.")

            if info.type.name not in {"int", "real", "str"} or info.type.is_array:
                self.error(arg, "input aceita apenas variaveis int, real ou str.")

    def visitConsoleLogStatement(self, ctx):
        if ctx.argumentList() is None:
            return

        for expr in ctx.argumentList().expression():
            self.expression_info(expr)

    # ======================================================
    # Expressoes
    # ======================================================

    def expression_info(self, ctx) -> ExprInfo:
        name = type(ctx).__name__

        if name == "ExpressionContext":
            return self.expression_info(ctx.assignmentExpression())

        if name == "AssignmentExpressionContext":
            if ctx.assignmentOperator() is not None:
                left = self.postfix_info(ctx.postfixExpression())

                if not left.is_lvalue:
                    self.error(ctx.postfixExpression(), "lado esquerdo da atribuicao deve ser atribuivel.")

                if left.is_const:
                    self.error(ctx.postfixExpression(), "nao e permitido alterar constante.")

                right = self.expression_info(ctx.assignmentExpression())
                op = ctx.assignmentOperator().getText()

                if op == "=":
                    if not can_assign(left.type, right.type, self.known_classes):
                        self.error(
                            ctx,
                            f"atribuicao incompativel: '{left.type}' recebe '{right.type}'."
                        )
                    return ExprInfo(left.type)

                if op in {"+=", "-=", "*=", "/=", "%=", "**=", "&&=", "||="}:
                    self.validate_compound_assignment(ctx, left.type, right.type, op)
                    return ExprInfo(left.type)

            return self.expression_info(ctx.logicalOrExpression())

        if name == "LogicalOrExpressionContext":
            expressions = ctx.logicalAndExpression()
            result = self.expression_info(expressions[0]).type

            for expr in expressions[1:]:
                right = self.expression_info(expr).type
                if result != BOOL or right != BOOL:
                    self.error(ctx, "operador || exige operandos bool.")
                result = BOOL

            return ExprInfo(result)

        if name == "LogicalAndExpressionContext":
            expressions = ctx.equalityExpression()
            result = self.expression_info(expressions[0]).type

            for expr in expressions[1:]:
                right = self.expression_info(expr).type
                if result != BOOL or right != BOOL:
                    self.error(ctx, "operador && exige operandos bool.")
                result = BOOL

            return ExprInfo(result)

        if name == "EqualityExpressionContext":
            expressions = ctx.relationalExpression()
            result = self.expression_info(expressions[0]).type

            for expr in expressions[1:]:
                right = self.expression_info(expr).type
                if not self.types_comparable(result, right):
                    self.error(ctx, f"comparacao invalida entre '{result}' e '{right}'.")
                result = BOOL

            return ExprInfo(result)

        if name == "RelationalExpressionContext":
            expressions = ctx.additiveExpression()
            result = self.expression_info(expressions[0]).type

            for expr in expressions[1:]:
                right = self.expression_info(expr).type
                if result.is_array or right.is_array:
                    self.error(ctx, "operadores relacionais nao aceitam vetores.")
                if result == VOID or right == VOID:
                    self.error(ctx, "operadores relacionais nao aceitam void.")
                result = BOOL

            return ExprInfo(result)

        if name == "AdditiveExpressionContext":
            expressions = ctx.multiplicativeExpression()
            result = self.expression_info(expressions[0]).type

            for i, expr in enumerate(expressions[1:], start=1):
                op = ctx.getChild(2 * i - 1).getText()
                right = self.expression_info(expr).type

                if op == "+":
                    if result.name == "str" or right.name == "str":
                        if result.is_array or right.is_array:
                            self.error(ctx, "concatenacao nao aceita vetores.")
                        result = STR
                    elif result.is_numeric() and right.is_numeric():
                        result = numeric_result(result, right)
                    else:
                        self.error(ctx, f"operador + invalido entre '{result}' e '{right}'.")

                elif op == "-":
                    if not (result.is_numeric() and right.is_numeric()):
                        self.error(ctx, "operador - exige operandos numericos.")
                    result = numeric_result(result, right)

            return ExprInfo(result)

        if name == "MultiplicativeExpressionContext":
            expressions = ctx.powerExpression()
            result = self.expression_info(expressions[0]).type

            for i, expr in enumerate(expressions[1:], start=1):
                op = ctx.getChild(2 * i - 1).getText()
                right = self.expression_info(expr).type

                if op in {"*", "/"}:
                    if not (result.is_numeric() and right.is_numeric()):
                        self.error(ctx, f"operador {op} exige operandos numericos.")
                    result = numeric_result(result, right)

                elif op == "%":
                    if result != INT or right != INT:
                        self.error(ctx, "operador % exige operandos int.")
                    result = INT

            return ExprInfo(result)

        if name == "PowerExpressionContext":
            left = self.expression_info(ctx.unaryExpression()).type

            if ctx.powerExpression() is not None:
                right = self.expression_info(ctx.powerExpression()).type

                if left != INT or right != INT:
                    self.error(ctx, "operador ** exige operandos int.")

                return ExprInfo(INT)

            return ExprInfo(left)

        if name == "UnaryExpressionContext":
            if ctx.postfixExpression() is not None:
                return self.postfix_info(ctx.postfixExpression())

            inner = self.expression_info(ctx.unaryExpression())

            if ctx.NOT() is not None:
                if inner.type != BOOL:
                    self.error(ctx, "operador ! exige operando bool.")
                return ExprInfo(BOOL)

            if ctx.PLUS() is not None or ctx.MINUS() is not None:
                if not inner.type.is_numeric():
                    self.error(ctx, "operador unario + ou - exige operando numerico.")
                return ExprInfo(inner.type)

            if ctx.INC() is not None or ctx.DEC() is not None:
                if not inner.is_lvalue:
                    self.error(ctx, "operador ++ ou -- exige variavel atribuivel.")
                if inner.is_const:
                    self.error(ctx, "nao e permitido aplicar ++ ou -- em constante.")
                if not inner.type.is_numeric():
                    self.error(ctx, "operador ++ ou -- exige operando numerico.")
                return ExprInfo(inner.type)

        if name == "PostfixExpressionContext":
            return self.postfix_info(ctx)

        if name == "PrimaryExpressionContext":
            return self.primary_info(ctx)

        self.error(ctx, f"expressao nao reconhecida internamente: {name}")

    def postfix_info(self, ctx) -> ExprInfo:
        info = self.primary_info(ctx.primaryExpression())

        for suffix in ctx.postfixSuffix():
            if suffix.LBRACK() is not None:
                index_type = self.expression_info(suffix.expression()).type

                if index_type != INT:
                    self.error(suffix, "indice de vetor deve ser int.")

                if not info.type.is_array:
                    self.error(suffix, f"tipo '{info.type}' nao e vetor.")

                info = ExprInfo(
                    type=info.type.element_type(),
                    symbol=info.symbol,
                    is_lvalue=True,
                    is_const=info.is_const
                )

            elif suffix.DOT() is not None and suffix.LPAREN() is not None:
                method_name = suffix.ID().getText()
                class_symbol = self.scopes.resolve_global(info.type.name)

                if class_symbol is None or class_symbol.kind != "class":
                    self.error(suffix, f"tipo '{info.type}' nao possui metodos.")

                method_symbol = class_symbol.methods.get(method_name)

                if method_symbol is None:
                    self.error(suffix, f"metodo '{method_name}' nao existe na classe '{info.type.name}'.")

                arg_types = self.argument_types(suffix.argumentList())
                self.validate_call_arguments(suffix, method_symbol.params, arg_types, method_name)

                info = ExprInfo(type=method_symbol.return_type or VOID)

            elif suffix.DOT() is not None:
                field_name = suffix.ID().getText()
                class_symbol = self.scopes.resolve_global(info.type.name)

                if class_symbol is None or class_symbol.kind != "class":
                    self.error(suffix, f"tipo '{info.type}' nao possui atributos.")

                field_symbol = class_symbol.fields.get(field_name)

                if field_symbol is None:
                    self.error(suffix, f"atributo '{field_name}' nao existe na classe '{info.type.name}'.")

                info = ExprInfo(
                    type=field_symbol.type,
                    symbol=field_symbol,
                    is_lvalue=True,
                    is_const=info.is_const
                )

            elif suffix.LPAREN() is not None:
                if info.symbol is None or info.symbol.kind != "function":
                    self.error(suffix, "chamada invalida: identificador nao e funcao.")

                arg_types = self.argument_types(suffix.argumentList())
                self.validate_call_arguments(suffix, info.symbol.params, arg_types, info.symbol.name)

                info = ExprInfo(type=info.symbol.return_type or VOID)

            elif suffix.INC() is not None or suffix.DEC() is not None:
                if not info.is_lvalue:
                    self.error(suffix, "operador ++ ou -- exige variavel atribuivel.")

                if info.is_const:
                    self.error(suffix, "nao e permitido aplicar ++ ou -- em constante.")

                if not info.type.is_numeric():
                    self.error(suffix, "operador ++ ou -- exige operando numerico.")

                # Pos-incremento/pos-decremento produz um valor, mas o resultado
                # da expressao nao deve continuar sendo atribuivel.
                info = ExprInfo(type=info.type, is_lvalue=False, is_const=False)

        return info

    def primary_info(self, ctx) -> ExprInfo:
        if ctx.literal() is not None:
            return ExprInfo(self.literal_type(ctx.literal()))

        if ctx.ID() is not None:
            name = ctx.ID().getText()
            symbol = self.scopes.resolve(name)

            if symbol is None:
                self.error(ctx, f"identificador '{name}' nao declarado.")

            is_lvalue = symbol.kind in {"variable", "constant", "parameter", "field", "this"}
            return ExprInfo(
                type=symbol.return_type if symbol.kind == "function" else symbol.type,
                symbol=symbol,
                is_lvalue=is_lvalue,
                is_const=symbol.is_const
            )

        if ctx.THIS() is not None:
            symbol = self.scopes.resolve("this")

            if symbol is None:
                self.error(ctx, "this so pode ser usado dentro de classe.")

            return ExprInfo(type=symbol.type, symbol=symbol)

        if ctx.newExpression() is not None:
            return self.new_expression_info(ctx.newExpression())

        if ctx.castExpression() is not None:
            return self.cast_expression_info(ctx.castExpression())

        if ctx.expression() is not None:
            return self.expression_info(ctx.expression())

        self.error(ctx, "expressao primaria invalida.")

    def literal_type(self, ctx) -> JssType:
        if ctx.INT_LITERAL() is not None:
            return INT
        if ctx.REAL_LITERAL() is not None:
            return REAL
        if ctx.STRING_LITERAL() is not None:
            return STR
        if ctx.TRUE() is not None or ctx.FALSE() is not None:
            return BOOL
        if ctx.NULL() is not None:
            return NULL

        self.error(ctx, "literal invalido.")

    def new_expression_info(self, ctx) -> ExprInfo:
        class_name = ctx.ID().getText()
        class_symbol = self.scopes.resolve_global(class_name)

        if class_symbol is None or class_symbol.kind != "class":
            self.error(ctx, f"classe '{class_name}' nao declarada.")

        arg_types = self.argument_types(ctx.argumentList())
        self.validate_call_arguments(ctx, class_symbol.constructor_params, arg_types, class_name)

        return ExprInfo(JssType(class_name))

    def cast_expression_info(self, ctx) -> ExprInfo:
        target_type = JssType(ctx.primitiveType().getText())
        source_type = self.expression_info(ctx.expression()).type

        if not can_cast(source_type, target_type):
            self.error(ctx, f"conversao invalida de '{source_type}' para '{target_type}'.")

        return ExprInfo(target_type)

    def argument_types(self, argument_list_ctx) -> list[JssType]:
        if argument_list_ctx is None:
            return []

        return [self.expression_info(expr).type for expr in argument_list_ctx.expression()]

    def validate_call_arguments(self, ctx, params: list[tuple[str, JssType]], args: list[JssType], function_name: str):
        if len(params) != len(args):
            self.error(
                ctx,
                f"chamada de '{function_name}' espera {len(params)} argumento(s), "
                f"mas recebeu {len(args)}."
            )

        for index, ((_, expected), actual) in enumerate(zip(params, args), start=1):
            if not can_assign(expected, actual, self.known_classes):
                self.error(
                    ctx,
                    f"argumento {index} de '{function_name}' deveria ser '{expected}', "
                    f"mas recebeu '{actual}'."
                )

    def validate_compound_assignment(self, ctx, left: JssType, right: JssType, op: str):
        if op == "+=":
            if left.name == "str":
                return
            if left.is_numeric() and right.is_numeric():
                return
            self.error(ctx, f"operador += invalido entre '{left}' e '{right}'.")

        if op in {"-=", "*=", "/="}:
            if left.is_numeric() and right.is_numeric():
                return
            self.error(ctx, f"operador {op} exige operandos numericos.")

        if op == "%=":
            if left == INT and right == INT:
                return
            self.error(ctx, "operador %= exige operandos int.")

        if op == "**=":
            if left == INT and right == INT:
                return
            self.error(ctx, "operador **= exige operandos int.")

        if op in {"&&=", "||="}:
            if left == BOOL and right == BOOL:
                return
            self.error(ctx, f"operador {op} exige operandos bool.")

    def types_comparable(self, left: JssType, right: JssType) -> bool:
        if left.is_array or right.is_array:
            return False

        if left == right:
            return True

        if left.is_numeric() and right.is_numeric():
            return True

        if left == NULL and right.name in self.known_classes:
            return True

        if right == NULL and left.name in self.known_classes:
            return True

        return False