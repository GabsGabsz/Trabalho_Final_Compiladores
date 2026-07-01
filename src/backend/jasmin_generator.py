# pyright: reportOptionalMemberAccess=false
# pyright: reportOptionalIterable=false
# pyright: reportArgumentType=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportAttributeAccessIssue=false

from dataclasses import dataclass, field
from pathlib import Path

from JSSParserVisitor import JSSParserVisitor

from backend.code_writer import CodeWriter
from backend.label_manager import LabelManager

PRIMITIVE_TYPES = {"int", "real", "str", "bool", "void"}


@dataclass
class VarInfo:
    name: str
    type_name: str
    slot: int | None = None
    is_global: bool = False
    array_size: int | None = None
    array_sizes: list[int] | None = None

    @property
    def descriptor(self) -> str:
        return jasmin_descriptor(self.type_name)


@dataclass
class LValue:
    kind: str
    type_name: str
    var: VarInfo | None = None
    owner_type: str | None = None
    field_name: str | None = None


@dataclass
class FunctionInfo:
    name: str
    return_type: str
    param_types: list[str]

    @property
    def descriptor(self) -> str:
        params = "".join(jasmin_descriptor(t) for t in self.param_types)
        ret = jasmin_descriptor(self.return_type)
        return f"({params}){ret}"


@dataclass
class FieldInfo:
    name: str
    type_name: str
    array_size: int | None = None
    array_sizes: list[int] | None = None

    @property
    def descriptor(self) -> str:
        return jasmin_descriptor(self.type_name)


@dataclass
class MethodInfo:
    name: str
    return_type: str
    param_types: list[str]
    ctx: object | None = None

    @property
    def descriptor(self) -> str:
        params = "".join(jasmin_descriptor(t) for t in self.param_types)
        ret = jasmin_descriptor(self.return_type)
        return f"({params}){ret}"


@dataclass
class ConstructorInfo:
    param_types: list[str] = field(default_factory=list)
    ctx: object | None = None

    @property
    def descriptor(self) -> str:
        params = "".join(jasmin_descriptor(t) for t in self.param_types)
        return f"({params})V"


@dataclass
class ClassInfo:
    name: str
    fields: dict[str, FieldInfo] = field(default_factory=dict)
    methods: dict[str, MethodInfo] = field(default_factory=dict)
    constructor: ConstructorInfo = field(default_factory=ConstructorInfo)
    ctx: object | None = None


class MethodContext:
    def __init__(
        self,
        name: str,
        return_type: str,
        start_slot: int,
        owner_class: str | None = None,
    ):
        self.name = name
        self.return_type = return_type
        self.owner_class = owner_class
        self.locals: dict[str, VarInfo] = {}
        self.next_slot = start_slot
        self.break_labels: list[str] = []

    def add_local(
        self,
        name: str,
        type_name: str,
        array_size: int | None = None,
        array_sizes: list[int] | None = None,
    ) -> VarInfo:
        var = VarInfo(
            name=name,
            type_name=type_name,
            slot=self.next_slot,
            is_global=False,
            array_size=array_size,
            array_sizes=array_sizes,
        )

        self.locals[name] = var

        # double ocupa 2 slots; arrays e objetos sao referencias e ocupam 1 slot.
        if type_name == "real":
            self.next_slot += 2
        else:
            self.next_slot += 1

        return var

    def resolve_local(self, name: str) -> VarInfo | None:
        return self.locals.get(name)


# ==========================================================
# Descritores Jasmin/JVM
# ==========================================================


def is_array_type(type_name: str) -> bool:
    return type_name.endswith("[]")


def array_element_type(type_name: str) -> str:
    return type_name[:-2]


def is_reference_type(type_name: str) -> bool:
    return (
        type_name == "str"
        or is_array_type(type_name)
        or type_name not in PRIMITIVE_TYPES
    )


def jasmin_descriptor(type_name: str) -> str:
    if is_array_type(type_name):
        return "[" + jasmin_descriptor(array_element_type(type_name))

    if type_name == "int":
        return "I"
    if type_name == "real":
        return "D"
    if type_name == "bool":
        return "Z"
    if type_name == "str":
        return "Ljava/lang/String;"
    if type_name == "void":
        return "V"

    return f"L{type_name};"


def jasmin_newarray_instruction(base_type: str) -> str:
    if base_type == "int":
        return "newarray int"
    if base_type == "real":
        return "newarray double"
    if base_type == "bool":
        return "newarray boolean"
    if base_type == "str":
        return "anewarray java/lang/String"
    if is_array_type(base_type):
        return f"anewarray {jasmin_descriptor(base_type)}"

    return f"anewarray {base_type}"


def jasmin_array_load_instruction(base_type: str) -> str:
    if base_type in {"int", "bool"}:
        return "iaload"
    if base_type == "real":
        return "daload"
    return "aaload"


def jasmin_array_store_instruction(base_type: str) -> str:
    if base_type in {"int", "bool"}:
        return "iastore"
    if base_type == "real":
        return "dastore"
    return "aastore"


class JasminGenerator(JSSParserVisitor):
    def __init__(self, class_name: str = "Main"):
        super().__init__()
        self.class_name = class_name
        self.writer = CodeWriter()
        self.labels = LabelManager()

        self.output_dir = Path("output")

        self.globals: dict[str, VarInfo] = {}
        self.global_initializers = []

        self.functions: dict[str, FunctionInfo] = {}
        self.classes: dict[str, ClassInfo] = {}

        self.current_method: MethodContext | None = None
        self.current_class: ClassInfo | None = None

    def generate(self, tree, output_path: str | Path = "output/Main.j") -> Path:
        output_path = Path(output_path)
        self.output_dir = output_path.parent
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Evita montar .j antigo de testes anteriores.
        for old_file in self.output_dir.glob("*.j"):
            old_file.unlink()

        self.collect_globals_functions_and_classes(tree)

        # Primeiro gera as classes JSS separadas: Ponto.j, Pessoa.j etc.
        self.emit_class_files(tree)

        # Depois gera a classe Main com funcoes globais e main Java.
        self.writer = CodeWriter()
        self.emit_main_class_header()
        self.emit_main_fields()
        self.emit_main_constructor()
        self.emit_static_initializer()
        self.emit_functions(tree)

        self.writer.save(output_path)
        return output_path

    # ======================================================
    # Coleta inicial
    # ======================================================

    def collect_globals_functions_and_classes(self, program_ctx):
        # Primeira passada: registra os nomes das classes para permitir tipos de objeto.
        for top in program_ctx.topLevelDeclaration():
            class_ctx = top.classDeclaration()
            if class_ctx is not None:
                name = class_ctx.ID().getText()
                self.classes[name] = ClassInfo(name=name, ctx=class_ctx)

        # Segunda passada: coleta membros de classes, globais e funcoes.
        for top in program_ctx.topLevelDeclaration():
            class_ctx = top.classDeclaration()
            stmt_ctx = top.statement()
            var_ctx = stmt_ctx.variableDeclaration() if stmt_ctx is not None else None
            func_ctx = top.functionDeclaration()

            if class_ctx is not None:
                self.collect_class_members(class_ctx)

            elif var_ctx is not None:
                type_name = self.type_name_from_type_ctx(var_ctx.type_())
                array_size = self.array_size_from_type_ctx(var_ctx.type_())
                array_sizes = self.array_sizes_from_type_ctx(var_ctx.type_())

                for declarator in var_ctx.variableDeclarator():
                    name = declarator.ID().getText()

                    self.globals[name] = VarInfo(
                        name=name,
                        type_name=type_name,
                        slot=None,
                        is_global=True,
                        array_size=array_size,
                        array_sizes=array_sizes,
                    )

                    self.global_initializers.append((type_name, declarator))

            elif func_ctx is not None:
                name = func_ctx.ID().getText()
                return_type = self.type_name_from_return_type_ctx(func_ctx.returnType())
                param_types = self.param_types(func_ctx.parameterList())

                self.functions[name] = FunctionInfo(
                    name=name,
                    return_type=return_type,
                    param_types=param_types,
                )

    # Mantem compatibilidade com chamadas antigas, caso existam.
    def collect_globals_and_functions(self, program_ctx):
        self.collect_globals_functions_and_classes(program_ctx)

    def collect_class_members(self, class_ctx):
        class_name = class_ctx.ID().getText()
        class_info = self.classes[class_name]

        for member in class_ctx.classMember():
            field_ctx = member.fieldDeclaration()
            constructor_ctx = member.constructorDeclaration()
            method_ctx = member.methodDeclaration()

            if field_ctx is not None:
                field_name = field_ctx.ID().getText()
                field_type = self.type_name_from_type_ctx(field_ctx.type_())
                field_array_size = self.array_size_from_type_ctx(field_ctx.type_())
                field_array_sizes = self.array_sizes_from_type_ctx(field_ctx.type_())
                class_info.fields[field_name] = FieldInfo(
                    name=field_name,
                    type_name=field_type,
                    array_size=field_array_size,
                    array_sizes=field_array_sizes,
                )

            elif constructor_ctx is not None:
                param_types = self.param_types(constructor_ctx.parameterList())
                class_info.constructor = ConstructorInfo(
                    param_types=param_types, ctx=constructor_ctx
                )

            elif method_ctx is not None:
                method_name = method_ctx.ID().getText()
                return_type = self.type_name_from_return_type_ctx(
                    method_ctx.returnType()
                )
                param_types = self.param_types(method_ctx.parameterList())
                class_info.methods[method_name] = MethodInfo(
                    name=method_name,
                    return_type=return_type,
                    param_types=param_types,
                    ctx=method_ctx,
                )

    def type_name_from_type_ctx(self, ctx) -> str:
        base = ctx.baseType().getText()
        sizes = self.array_sizes_from_type_ctx(ctx)

        if sizes:
            return base + "[]" * len(sizes)

        return base

    def array_sizes_from_type_ctx(self, ctx) -> list[int]:
        if ctx.arraySuffix() is None:
            return []

        return [int(tok.getText()) for tok in ctx.arraySuffix().INT_LITERAL()]

    def array_size_from_type_ctx(self, ctx) -> int | None:
        sizes = self.array_sizes_from_type_ctx(ctx)
        return sizes[0] if sizes else None

    def type_name_from_return_type_ctx(self, ctx) -> str:
        if ctx.VOID() is not None:
            return "void"

        return self.type_name_from_type_ctx(ctx.type_())

    def param_types(self, parameter_list_ctx) -> list[str]:
        if parameter_list_ctx is None:
            return []

        return [
            self.type_name_from_type_ctx(param.type_())
            for param in parameter_list_ctx.parameter()
        ]

    # ======================================================
    # Classe Main
    # ======================================================

    def emit_main_class_header(self):
        self.writer.emit(f".class public {self.class_name}")
        self.writer.emit(".super java/lang/Object")
        self.writer.emit()

    # Mantem compatibilidade com o nome antigo.
    def emit_class_header(self):
        self.emit_main_class_header()

    def emit_main_fields(self):
        self.writer.emit(".field static __scanner Ljava/util/Scanner;")

        for var in self.globals.values():
            self.writer.emit(f".field static {var.name} {var.descriptor}")

        self.writer.emit()

    # Mantem compatibilidade com o nome antigo.
    def emit_fields(self):
        self.emit_main_fields()

    def emit_main_constructor(self):
        self.writer.emit(".method public <init>()V")
        self.writer.indent()
        self.writer.emit("aload_0")
        self.writer.emit("invokespecial java/lang/Object/<init>()V")
        self.writer.emit("return")
        self.writer.dedent()
        self.writer.emit(".end method")
        self.writer.emit()

    # Mantem compatibilidade com o nome antigo.
    def emit_constructor(self):
        self.emit_main_constructor()

    def emit_static_initializer(self):
        self.writer.emit(".method static <clinit>()V")
        self.writer.indent()
        self.writer.emit(".limit stack 300")
        self.writer.emit(".limit locals 20")

        # Inicializa o Scanner: __scanner = new Scanner(System.in).useLocale(Locale.US)
        self.writer.emit("new java/util/Scanner")
        self.writer.emit("dup")
        self.writer.emit("getstatic java/lang/System/in Ljava/io/InputStream;")
        self.writer.emit(
            "invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V"
        )
        self.writer.emit("getstatic java/util/Locale/US Ljava/util/Locale;")
        self.writer.emit(
            "invokevirtual java/util/Scanner/useLocale(Ljava/util/Locale;)Ljava/util/Scanner;"
        )
        self.writer.emit(f"putstatic {self.class_name}/__scanner Ljava/util/Scanner;")

        for type_name, declarator in self.global_initializers:
            name = declarator.ID().getText()
            var = self.globals[name]
            initializer = declarator.initializer()

            if is_array_type(var.type_name):
                if initializer is not None and initializer.expression() is not None:
                    self.gen_expression(initializer.expression())
                    self.emit_store_var(var)
                    continue

                if var.array_size is None:
                    raise NotImplementedError(
                        "Vetor global sem tamanho nao suportado no back-end."
                    )

                self.emit_array_creation_with_initializer(
                    var.type_name, var.array_sizes or [var.array_size], initializer
                )
                self.emit_store_var(var)
                continue

            if initializer is not None and initializer.expression() is not None:
                expr_type = self.gen_expression(initializer.expression())

                if var.type_name == "real" and expr_type == "int":
                    self.writer.emit("i2d")
            else:
                self.emit_default_value(type_name)

            self.emit_store_var(var)

        self.writer.emit("return")
        self.writer.dedent()
        self.writer.emit(".end method")
        self.writer.emit()

    def emit_functions(self, program_ctx):
        found_main = False

        for top in program_ctx.topLevelDeclaration():
            func_ctx = top.functionDeclaration()

            if func_ctx is not None:
                name = func_ctx.ID().getText()

                if name == "main":
                    found_main = True
                    self.emit_java_main(func_ctx)
                else:
                    self.emit_function(func_ctx)

        if not found_main:
            self.emit_top_level_main(program_ctx)

    def emit_top_level_main(self, program_ctx):
        self.current_method = MethodContext("main", "void", start_slot=1)

        self.writer.emit(".method public static main([Ljava/lang/String;)V")
        self.writer.indent()
        self.writer.emit(".limit stack 300")
        self.writer.emit(".limit locals 300")

        for top in program_ctx.topLevelDeclaration():
            stmt_ctx = top.statement()
            if stmt_ctx is not None and stmt_ctx.variableDeclaration() is None:
                self.gen_statement(stmt_ctx)

        self.writer.emit("return")
        self.writer.dedent()
        self.writer.emit(".end method")
        self.writer.emit()

        self.current_method = None

    def emit_empty_main(self):
        self.writer.emit(".method public static main([Ljava/lang/String;)V")
        self.writer.indent()
        self.writer.emit(".limit stack 10")
        self.writer.emit(".limit locals 1")
        self.writer.emit("return")
        self.writer.dedent()
        self.writer.emit(".end method")
        self.writer.emit()

    # ======================================================
    # Classes JSS
    # ======================================================

    def emit_class_files(self, program_ctx):
        for top in program_ctx.topLevelDeclaration():
            class_ctx = top.classDeclaration()
            if class_ctx is not None:
                self.emit_single_class_file(class_ctx)

    def emit_single_class_file(self, class_ctx):
        old_writer = self.writer
        old_method = self.current_method
        old_class = self.current_class

        class_name = class_ctx.ID().getText()
        class_info = self.classes[class_name]

        self.writer = CodeWriter()
        self.current_class = class_info
        self.current_method = None

        self.writer.emit(f".class public {class_name}")
        self.writer.emit(".super java/lang/Object")
        self.writer.emit()

        for field_info in class_info.fields.values():
            self.writer.emit(f".field public {field_info.name} {field_info.descriptor}")

        if class_info.fields:
            self.writer.emit()

        self.emit_jss_constructor(class_info)

        for method_info in class_info.methods.values():
            self.emit_jss_method(class_info, method_info)

        self.writer.save(self.output_dir / f"{class_name}.j")

        self.writer = old_writer
        self.current_method = old_method
        self.current_class = old_class

    def emit_jss_constructor(self, class_info: ClassInfo):
        constructor = class_info.constructor
        ctx = constructor.ctx

        self.current_method = MethodContext(
            "<init>", "void", start_slot=1, owner_class=class_info.name
        )

        if ctx is not None and ctx.parameterList() is not None:
            for param_ctx in ctx.parameterList().parameter():
                param_name = param_ctx.ID().getText()
                param_type = self.type_name_from_type_ctx(param_ctx.type_())
                param_array_size = self.array_size_from_type_ctx(param_ctx.type_())
                param_array_sizes = self.array_sizes_from_type_ctx(param_ctx.type_())
                self.current_method.add_local(
                    param_name,
                    param_type,
                    array_size=param_array_size,
                    array_sizes=param_array_sizes,
                )

        self.writer.emit(f".method public <init>{constructor.descriptor}")
        self.writer.indent()
        self.writer.emit(".limit stack 300")
        self.writer.emit(".limit locals 300")

        self.writer.emit("aload_0")
        self.writer.emit("invokespecial java/lang/Object/<init>()V")

        # Inicializa automaticamente atributos que sao vetores com tamanho fixo.
        for field_info in class_info.fields.values():
            if is_array_type(field_info.type_name) and field_info.array_sizes:
                self.writer.emit("aload_0")
                self.emit_array_creation_with_initializer(
                    field_info.type_name, field_info.array_sizes, None
                )
                self.writer.emit(
                    f"putfield {class_info.name}/{field_info.name} {field_info.descriptor}"
                )

        if ctx is not None:
            self.gen_block(ctx.block())

        self.writer.emit("return")
        self.writer.dedent()
        self.writer.emit(".end method")
        self.writer.emit()

        self.current_method = None

    def emit_jss_method(self, class_info: ClassInfo, method_info: MethodInfo):
        ctx = method_info.ctx
        self.current_method = MethodContext(
            method_info.name,
            method_info.return_type,
            start_slot=1,
            owner_class=class_info.name,
        )

        if ctx is not None and ctx.parameterList() is not None:
            for param_ctx in ctx.parameterList().parameter():
                param_name = param_ctx.ID().getText()
                param_type = self.type_name_from_type_ctx(param_ctx.type_())
                param_array_size = self.array_size_from_type_ctx(param_ctx.type_())
                param_array_sizes = self.array_sizes_from_type_ctx(param_ctx.type_())
                self.current_method.add_local(
                    param_name,
                    param_type,
                    array_size=param_array_size,
                    array_sizes=param_array_sizes,
                )

        self.writer.emit(f".method public {method_info.name}{method_info.descriptor}")
        self.writer.indent()
        self.writer.emit(".limit stack 300")
        self.writer.emit(".limit locals 300")

        if ctx is not None:
            self.gen_block(ctx.block())

        self.emit_default_return(method_info.return_type)

        self.writer.dedent()
        self.writer.emit(".end method")
        self.writer.emit()

        self.current_method = None

    # ======================================================
    # Funcoes globais
    # ======================================================

    def emit_java_main(self, func_ctx):
        self.current_method = MethodContext("main", "void", start_slot=1)

        self.writer.emit(".method public static main([Ljava/lang/String;)V")
        self.writer.indent()
        self.writer.emit(".limit stack 300")
        self.writer.emit(".limit locals 300")

        self.gen_block(func_ctx.block())

        self.writer.emit("return")
        self.writer.dedent()
        self.writer.emit(".end method")
        self.writer.emit()

        self.current_method = None

    def emit_function(self, func_ctx):
        name = func_ctx.ID().getText()
        info = self.functions[name]

        self.current_method = MethodContext(name, info.return_type, start_slot=0)

        params = (
            func_ctx.parameterList().parameter()
            if func_ctx.parameterList() is not None
            else []
        )

        for param_ctx in params:
            param_name = param_ctx.ID().getText()
            param_type = self.type_name_from_type_ctx(param_ctx.type_())
            param_array_size = self.array_size_from_type_ctx(param_ctx.type_())
            param_array_sizes = self.array_sizes_from_type_ctx(param_ctx.type_())
            self.current_method.add_local(
                param_name,
                param_type,
                array_size=param_array_size,
                array_sizes=param_array_sizes,
            )

        self.writer.emit(f".method public static {name}{info.descriptor}")
        self.writer.indent()
        self.writer.emit(".limit stack 300")
        self.writer.emit(".limit locals 300")

        self.gen_block(func_ctx.block())

        self.emit_default_return(info.return_type)

        self.writer.dedent()
        self.writer.emit(".end method")
        self.writer.emit()

        self.current_method = None

    def emit_default_return(self, return_type: str):
        if return_type == "void":
            self.writer.emit("return")
        elif return_type in {"int", "bool"}:
            self.writer.emit("iconst_0")
            self.writer.emit("ireturn")
        elif return_type == "real":
            self.writer.emit("dconst_0")
            self.writer.emit("dreturn")
        elif return_type == "str":
            self.writer.emit('ldc ""')
            self.writer.emit("areturn")
        else:
            self.writer.emit("aconst_null")
            self.writer.emit("areturn")

    # ======================================================
    # Blocos e comandos
    # ======================================================

    def gen_block(self, block_ctx):
        for statement in block_ctx.statement():
            self.gen_statement(statement)

    def gen_statement(self, ctx):
        if ctx.variableDeclaration() is not None:
            self.gen_variable_declaration(ctx.variableDeclaration())

        elif ctx.expression() is not None:
            result_type = self.gen_expression(ctx.expression())
            self.emit_pop_if_needed(result_type)

        elif ctx.consoleLogStatement() is not None:
            self.gen_console_log(ctx.consoleLogStatement())

        elif ctx.returnStatement() is not None:
            self.gen_return(ctx.returnStatement())

        elif ctx.ifStatement() is not None:
            self.gen_if(ctx.ifStatement())

        elif ctx.whileStatement() is not None:
            self.gen_while(ctx.whileStatement())

        elif ctx.forStatement() is not None:
            self.gen_for(ctx.forStatement())

        elif ctx.breakStatement() is not None:
            self.gen_break(ctx.breakStatement())

        elif ctx.block() is not None:
            self.gen_block(ctx.block())

        elif ctx.inputStatement() is not None:
            self.gen_input(ctx.inputStatement())

    def gen_variable_declaration(self, ctx):
        type_name = self.type_name_from_type_ctx(ctx.type_())
        array_size = self.array_size_from_type_ctx(ctx.type_())
        array_sizes = self.array_sizes_from_type_ctx(ctx.type_())

        for declarator in ctx.variableDeclarator():
            name = declarator.ID().getText()
            var = self.current_method.add_local(
                name, type_name, array_size=array_size, array_sizes=array_sizes
            )
            initializer = declarator.initializer()

            if is_array_type(type_name):
                if initializer is not None and initializer.expression() is not None:
                    self.gen_expression(initializer.expression())
                    self.emit_store_var(var)
                    continue

                if array_size is None:
                    raise NotImplementedError(
                        "Vetor sem tamanho nao suportado no back-end."
                    )

                self.emit_array_creation_with_initializer(
                    type_name, array_sizes, initializer
                )
                self.emit_store_var(var)
                continue

            if initializer is not None and initializer.expression() is not None:
                expr_type = self.gen_expression(initializer.expression())

                if var.type_name == "real" and expr_type == "int":
                    self.writer.emit("i2d")
            else:
                self.emit_default_value(type_name)

            self.emit_store_var(var)

    def gen_if(self, ctx):
        else_label = self.labels.new("else")
        end_label = self.labels.new("endif")

        self.gen_expression(ctx.expression())
        self.writer.emit(f"ifeq {else_label}")

        self.gen_block(ctx.block())

        self.writer.emit(f"goto {end_label}")
        self.writer.emit_label(else_label)

        for else_if in ctx.elseIfBlock():
            next_label = self.labels.new("elseif_next")

            self.gen_expression(else_if.expression())
            self.writer.emit(f"ifeq {next_label}")

            self.gen_block(else_if.block())

            self.writer.emit(f"goto {end_label}")
            self.writer.emit_label(next_label)

        if ctx.elseBlock() is not None:
            self.gen_block(ctx.elseBlock().block())

        self.writer.emit_label(end_label)

    def gen_while(self, ctx):
        start_label = self.labels.new("while_start")
        end_label = self.labels.new("while_end")

        self.writer.emit_label(start_label)
        self.gen_expression(ctx.expression())
        self.writer.emit(f"ifeq {end_label}")

        self.current_method.break_labels.append(end_label)
        self.gen_block(ctx.block())
        self.current_method.break_labels.pop()

        self.writer.emit(f"goto {start_label}")
        self.writer.emit_label(end_label)

    def gen_for(self, ctx):
        start_label = self.labels.new("for_start")
        end_label = self.labels.new("for_end")

        if ctx.forInit() is not None:
            if ctx.forInit().variableDeclaration() is not None:
                self.gen_variable_declaration(ctx.forInit().variableDeclaration())
            elif ctx.forInit().expression() is not None:
                result_type = self.gen_expression(ctx.forInit().expression())
                self.emit_pop_if_needed(result_type)

        self.writer.emit_label(start_label)

        if ctx.expression(0) is not None:
            self.gen_expression(ctx.expression(0))
            self.writer.emit(f"ifeq {end_label}")

        self.current_method.break_labels.append(end_label)
        self.gen_block(ctx.block())
        self.current_method.break_labels.pop()

        if ctx.expression(1) is not None:
            result_type = self.gen_expression(ctx.expression(1))
            self.emit_pop_if_needed(result_type)

        self.writer.emit(f"goto {start_label}")
        self.writer.emit_label(end_label)

    def gen_break(self, ctx):
        if not self.current_method.break_labels:
            raise RuntimeError("break sem rotulo de saida.")

        self.writer.emit(f"goto {self.current_method.break_labels[-1]}")

    def gen_return(self, ctx):
        expected = self.current_method.return_type

        if ctx.expression() is None:
            self.writer.emit("return")
            return

        actual = self.gen_expression(ctx.expression())

        if expected == "real" and actual == "int":
            self.writer.emit("i2d")

        if expected in {"int", "bool"}:
            self.writer.emit("ireturn")
        elif expected == "real":
            self.writer.emit("dreturn")
        elif expected == "str" or is_reference_type(expected):
            self.writer.emit("areturn")
        else:
            self.writer.emit("return")

    # ======================================================
    # console.log
    # ======================================================

    def gen_console_log(self, ctx):
        argument_list = ctx.argumentList()

        if argument_list is None:
            self.writer.emit("getstatic java/lang/System/out Ljava/io/PrintStream;")
            self.writer.emit("invokevirtual java/io/PrintStream/println()V")
            return

        expressions = argument_list.expression()

        for index, expr in enumerate(expressions):
            self.writer.emit("getstatic java/lang/System/out Ljava/io/PrintStream;")
            expr_type = self.gen_expression(expr)
            self.emit_print(expr_type)

            if index < len(expressions) - 1:
                self.writer.emit("getstatic java/lang/System/out Ljava/io/PrintStream;")
                self.writer.emit('ldc " "')
                self.writer.emit(
                    "invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V"
                )

        self.writer.emit("getstatic java/lang/System/out Ljava/io/PrintStream;")
        self.writer.emit("invokevirtual java/io/PrintStream/println()V")

    def emit_print(self, type_name: str):
        if type_name == "int":
            self.writer.emit("invokevirtual java/io/PrintStream/print(I)V")
        elif type_name == "real":
            self.writer.emit("invokevirtual java/io/PrintStream/print(D)V")
        elif type_name == "bool":
            self.writer.emit("invokevirtual java/io/PrintStream/print(Z)V")
        elif type_name == "str":
            self.writer.emit(
                "invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V"
            )
        else:
            self.writer.emit(
                "invokevirtual java/io/PrintStream/print(Ljava/lang/Object;)V"
            )

    # ======================================================
    # input
    # ======================================================

    def gen_input(self, ctx):
        input_list = ctx.inputArgumentList()

        if input_list is None:
            return

        for argument in input_list.inputArgument():
            target = self.resolve_lvalue(argument.postfixExpression())

            # Para vetor e atributo, resolve_lvalue ja deixa arrayref/indice
            # ou objectref na pilha antes de carregar o Scanner.
            self.writer.emit(f"getstatic {self.class_name}/__scanner Ljava/util/Scanner;")

            if target.type_name == "int":
                self.writer.emit("invokevirtual java/util/Scanner/nextInt()I")
            elif target.type_name == "real":
                self.writer.emit("invokevirtual java/util/Scanner/nextDouble()D")
            elif target.type_name == "str":
                self.writer.emit("invokevirtual java/util/Scanner/next()Ljava/lang/String;")
            else:
                raise NotImplementedError(
                    "Back-end Jasmin suporta input apenas para int, real e str."
                )

            self.emit_store_lvalue(target)

    # ======================================================
    # Expressoes
    # ======================================================

    def gen_expression(self, ctx) -> str:
        name = type(ctx).__name__

        if name == "ExpressionContext":
            return self.gen_expression(ctx.assignmentExpression())

        if name == "AssignmentExpressionContext":
            if ctx.assignmentOperator() is not None:
                op = ctx.assignmentOperator().getText()
                left = self.resolve_lvalue(ctx.postfixExpression())

                if op == "=":
                    right_type = self.gen_expression(ctx.assignmentExpression())

                    if left.type_name == "real" and right_type == "int":
                        self.writer.emit("i2d")

                    self.emit_store_lvalue(left)
                    return "void"

                if op in {"+=", "-=", "*=", "/=", "%=", "**=", "&&=", "||="}:
                    self.emit_load_lvalue_value(left)

                    right_type = self.gen_expression(ctx.assignmentExpression())

                    if left.type_name == "real" and right_type == "int":
                        self.writer.emit("i2d")

                    self.emit_compound_operation(op, left.type_name)
                    self.emit_store_lvalue(left)
                    return "void"

                raise NotImplementedError(
                    f"Back-end Jasmin ainda nao suporta operador de atribuicao composto {op}."
                )

            return self.gen_expression(ctx.logicalOrExpression())

        if name == "LogicalOrExpressionContext":
            expressions = ctx.logicalAndExpression()

            if len(expressions) == 1:
                return self.gen_expression(expressions[0])

            true_label = self.labels.new("or_true")
            end_label = self.labels.new("or_end")

            for expr in expressions:
                self.gen_expression(expr)
                self.writer.emit(f"ifne {true_label}")

            self.writer.emit("iconst_0")
            self.writer.emit(f"goto {end_label}")
            self.writer.emit_label(true_label)
            self.writer.emit("iconst_1")
            self.writer.emit_label(end_label)
            return "bool"

        if name == "LogicalAndExpressionContext":
            expressions = ctx.equalityExpression()

            if len(expressions) == 1:
                return self.gen_expression(expressions[0])

            false_label = self.labels.new("and_false")
            end_label = self.labels.new("and_end")

            for expr in expressions:
                self.gen_expression(expr)
                self.writer.emit(f"ifeq {false_label}")

            self.writer.emit("iconst_1")
            self.writer.emit(f"goto {end_label}")
            self.writer.emit_label(false_label)
            self.writer.emit("iconst_0")
            self.writer.emit_label(end_label)
            return "bool"

        if name == "EqualityExpressionContext":
            expressions = ctx.relationalExpression()
            result_type = self.gen_expression(expressions[0])

            for i, expr in enumerate(expressions[1:], start=1):
                op = ctx.getChild(2 * i - 1).getText()
                right_type = self.gen_expression(expr)
                self.emit_comparison(result_type, right_type, op)
                result_type = "bool"

            return result_type

        if name == "RelationalExpressionContext":
            expressions = ctx.additiveExpression()
            result_type = self.gen_expression(expressions[0])

            for i, expr in enumerate(expressions[1:], start=1):
                op = ctx.getChild(2 * i - 1).getText()
                right_type = self.gen_expression(expr)
                self.emit_comparison(result_type, right_type, op)
                result_type = "bool"

            return result_type

        if name == "AdditiveExpressionContext":
            expressions = ctx.multiplicativeExpression()
            result_type = self.gen_expression(expressions[0])

            for i, expr in enumerate(expressions[1:], start=1):
                op = ctx.getChild(2 * i - 1).getText()
                right_type = self.gen_expression(expr)

                if op == "+" and (result_type == "str" or right_type == "str"):
                    self.emit_string_concat(result_type, right_type)
                    result_type = "str"
                else:
                    result_type = self.prepare_numeric_binary_operands(
                        result_type, right_type
                    )
                    self.emit_numeric_operation(op, result_type)

            return result_type

        if name == "MultiplicativeExpressionContext":
            expressions = ctx.powerExpression()
            result_type = self.gen_expression(expressions[0])

            for i, expr in enumerate(expressions[1:], start=1):
                op = ctx.getChild(2 * i - 1).getText()
                right_type = self.gen_expression(expr)

                result_type = self.prepare_numeric_binary_operands(
                    result_type, right_type
                )

                if result_type == "real" and op == "%":
                    raise NotImplementedError(
                        "Operador % nao e suportado para real no back-end."
                    )

                self.emit_numeric_operation(op, result_type)

            return result_type

        if name == "PowerExpressionContext":
            left_type = self.gen_expression(ctx.unaryExpression())

            if ctx.powerExpression() is not None:
                original_left_type = left_type

                if left_type == "int":
                    self.writer.emit("i2d")
                elif left_type != "real":
                    raise NotImplementedError(
                        "Operador ** aceita apenas int ou real no back-end."
                    )

                right_type = self.gen_expression(ctx.powerExpression())
                original_right_type = right_type

                if right_type == "int":
                    self.writer.emit("i2d")
                elif right_type != "real":
                    raise NotImplementedError(
                        "Operador ** aceita apenas int ou real no back-end."
                    )

                self.writer.emit("invokestatic java/lang/Math/pow(DD)D")

                if original_left_type == "int" and original_right_type == "int":
                    self.writer.emit("d2i")
                    return "int"

                return "real"

            return left_type

        if name == "UnaryExpressionContext":
            if ctx.postfixExpression() is not None:
                return self.gen_postfix(ctx.postfixExpression())

            if ctx.INC() is not None or ctx.DEC() is not None:
                postfix = self.find_child_by_type_name(
                    ctx.unaryExpression(), "PostfixExpressionContext"
                )

                if postfix is None:
                    raise NotImplementedError(
                        "Incremento/decremento sem destino valido no back-end."
                    )

                target = self.resolve_lvalue(postfix)
                self.emit_load_lvalue_value(target)

                if target.type_name == "real":
                    self.writer.emit("dconst_1")
                else:
                    self.writer.emit("iconst_1")

                if ctx.INC() is not None:
                    self.emit_compound_operation("+=", target.type_name)
                else:
                    self.emit_compound_operation("-=", target.type_name)

                # Prefixo ++x/--x tambem produz o valor atualizado quando usado em expressao.
                if target.kind == "var":
                    if target.type_name == "real":
                        self.writer.emit("dup2")
                    else:
                        self.writer.emit("dup")
                    self.emit_store_lvalue(target)
                    return target.type_name

                self.emit_store_lvalue(target)
                return "void"

            inner_type = self.gen_expression(ctx.unaryExpression())

            if ctx.NOT() is not None:
                true_label = self.labels.new("not_true")
                end_label = self.labels.new("not_end")

                self.writer.emit(f"ifeq {true_label}")
                self.writer.emit("iconst_0")
                self.writer.emit(f"goto {end_label}")
                self.writer.emit_label(true_label)
                self.writer.emit("iconst_1")
                self.writer.emit_label(end_label)
                return "bool"

            if ctx.MINUS() is not None:
                if inner_type == "real":
                    self.writer.emit("dneg")
                    return "real"
                self.writer.emit("ineg")
                return "int"

            if ctx.PLUS() is not None:
                return inner_type

        if name == "PostfixExpressionContext":
            return self.gen_postfix(ctx)

        if name == "PrimaryExpressionContext":
            return self.gen_primary(ctx)

        raise NotImplementedError(f"Expressao nao suportada no back-end: {name}")

    def gen_postfix_inc_dec(self, ctx) -> str:
        suffixes = ctx.postfixSuffix()
        last_suffix = suffixes[-1]

        target = self.resolve_lvalue(ctx)

        if target.type_name not in {"int", "real"}:
            raise NotImplementedError(
                "Pos-incremento/pos-decremento aceita apenas int ou real no back-end."
            )

        # Carrega o valor antigo. Para vetor e atributo, resolve_lvalue ja deixou
        # arrayref/indice ou objectref na pilha; guardamos apenas o valor antigo
        # em temporario, preservando a referencia necessaria para o store.
        self.emit_load_lvalue_value(target)

        temp_slot = self.allocate_temp_slot(target.type_name)
        if target.type_name == "real":
            self.writer.emit(f"dstore {temp_slot}")
            self.writer.emit(f"dload {temp_slot}")
            self.writer.emit("dconst_1")
        else:
            self.writer.emit(f"istore {temp_slot}")
            self.writer.emit(f"iload {temp_slot}")
            self.writer.emit("iconst_1")

        if last_suffix.INC() is not None:
            self.emit_compound_operation("+=", target.type_name)
        else:
            self.emit_compound_operation("-=", target.type_name)

        self.emit_store_lvalue(target)

        # Como pos-incremento/pos-decremento e uma expressao, deixa na pilha
        # o valor antigo. Se for usado como comando isolado, gen_statement remove.
        if target.type_name == "real":
            self.writer.emit(f"dload {temp_slot}")
        else:
            self.writer.emit(f"iload {temp_slot}")

        return target.type_name

    def gen_postfix(self, ctx) -> str:
        primary = ctx.primaryExpression()
        suffixes = ctx.postfixSuffix()

        if not suffixes:
            return self.gen_primary(primary)

        if suffixes[-1].INC() is not None or suffixes[-1].DEC() is not None:
            return self.gen_postfix_inc_dec(ctx)

        # Chamada de funcao global: nome(...)
        if (
            len(suffixes) >= 1
            and suffixes[0].LPAREN() is not None
            and suffixes[0].DOT() is None
            and primary.ID() is not None
        ):
            func_name = primary.ID().getText()
            func_info = self.functions[func_name]

            arg_list = suffixes[0].argumentList()
            if arg_list is not None:
                for expr in arg_list.expression():
                    self.gen_expression(expr)

            self.writer.emit(
                f"invokestatic {self.class_name}/{func_name}{func_info.descriptor}"
            )
            current_type = func_info.return_type
            remaining_suffixes = suffixes[1:]
        else:
            current_type = self.gen_primary(primary)
            remaining_suffixes = suffixes

        for suffix in remaining_suffixes:
            if suffix.LBRACK() is not None:
                if not is_array_type(current_type):
                    raise NotImplementedError("Indexacao em variavel nao vetor no back-end.")

                element_type = array_element_type(current_type)
                index_expr = self.find_child_by_type_name(suffix, "ExpressionContext")
                if index_expr is None:
                    raise NotImplementedError("Indice de vetor nao encontrado no back-end.")

                self.gen_expression(index_expr)
                self.writer.emit(jasmin_array_load_instruction(element_type))
                current_type = element_type

            elif suffix.DOT() is not None and suffix.LPAREN() is not None:
                method_name = suffix.ID().getText()
                method_info = self.classes[current_type].methods[method_name]

                arg_list = suffix.argumentList()
                if arg_list is not None:
                    for expr in arg_list.expression():
                        self.gen_expression(expr)

                self.writer.emit(
                    f"invokevirtual {current_type}/{method_name}{method_info.descriptor}"
                )
                current_type = method_info.return_type

            elif suffix.DOT() is not None:
                field_name = suffix.ID().getText()
                field_info = self.classes[current_type].fields[field_name]
                self.writer.emit(
                    f"getfield {current_type}/{field_name} {field_info.descriptor}"
                )
                current_type = field_info.type_name

            else:
                raise NotImplementedError(
                    "Back-end Jasmin ainda nao suporta acesso encadeado complexo."
                )

        return current_type

    def gen_primary(self, ctx) -> str:
        if ctx.literal() is not None:
            return self.gen_literal(ctx.literal())

        if ctx.ID() is not None:
            var = self.resolve_variable(ctx.ID().getText())
            self.emit_load_var(var)
            return var.type_name

        if ctx.THIS() is not None:
            if self.current_method is None or self.current_method.owner_class is None:
                raise NotImplementedError("this fora de metodo de classe no back-end.")

            self.writer.emit("aload_0")
            return self.current_method.owner_class

        if ctx.newExpression() is not None:
            return self.gen_new_expression(ctx.newExpression())

        if ctx.expression() is not None:
            return self.gen_expression(ctx.expression())

        if ctx.castExpression() is not None:
            return self.gen_cast(ctx.castExpression())

        raise NotImplementedError("Expressao primaria ainda nao suportada no back-end.")

    def gen_new_expression(self, ctx) -> str:
        class_name = ctx.ID().getText()
        class_info = self.classes[class_name]
        constructor = class_info.constructor

        self.writer.emit(f"new {class_name}")
        self.writer.emit("dup")

        arg_list = ctx.argumentList()
        if arg_list is not None:
            for expr in arg_list.expression():
                self.gen_expression(expr)

        self.writer.emit(f"invokespecial {class_name}/<init>{constructor.descriptor}")
        return class_name

    def gen_literal(self, ctx) -> str:
        if ctx.INT_LITERAL() is not None:
            self.emit_push_int(int(ctx.INT_LITERAL().getText()))
            return "int"

        if ctx.REAL_LITERAL() is not None:
            self.writer.emit(f"ldc2_w {ctx.REAL_LITERAL().getText()}")
            return "real"

        if ctx.STRING_LITERAL() is not None:
            self.writer.emit(f"ldc {ctx.STRING_LITERAL().getText()}")
            return "str"

        if ctx.TRUE() is not None:
            self.writer.emit("iconst_1")
            return "bool"

        if ctx.FALSE() is not None:
            self.writer.emit("iconst_0")
            return "bool"

        if ctx.NULL() is not None:
            self.writer.emit("aconst_null")
            return "null"

        raise NotImplementedError("Literal nao suportado no back-end.")

    def gen_cast(self, ctx) -> str:
        target = ctx.primitiveType().getText()
        source = self.gen_expression(ctx.expression())

        if target == source:
            return target

        if target == "real" and source in {"int", "bool"}:
            self.writer.emit("i2d")
            return "real"

        if target == "int" and source == "real":
            self.writer.emit("d2i")
            return "int"

        if target == "int" and source == "bool":
            return "int"

        if target == "bool" and source == "int":
            self.emit_int_to_bool()
            return "bool"

        if target == "bool" and source == "real":
            self.emit_real_to_bool()
            return "bool"

        if target == "str":
            desc = jasmin_descriptor(source)
            self.writer.emit(
                f"invokestatic java/lang/String/valueOf({desc})Ljava/lang/String;"
            )
            return "str"

        raise NotImplementedError(
            f"Cast {source} para {target} ainda nao suportado no back-end."
        )

    # ======================================================
    # Variaveis, atributos e vetores
    # ======================================================

    def resolve_variable(self, name: str) -> VarInfo:
        if self.current_method is not None:
            local = self.current_method.resolve_local(name)
            if local is not None:
                return local

        if name in self.globals:
            return self.globals[name]

        raise RuntimeError(f"Variavel nao encontrada no back-end: {name}")

    def resolve_lvalue(self, postfix_ctx) -> LValue:
        primary = postfix_ctx.primaryExpression()
        suffixes = list(postfix_ctx.postfixSuffix())

        # Em x++ ou x--, o ultimo sufixo nao faz parte do destino de atribuicao;
        # ele apenas indica a operacao de incremento/decremento.
        if suffixes and (suffixes[-1].INC() is not None or suffixes[-1].DEC() is not None):
            suffixes = suffixes[:-1]

        # Variavel simples: x
        if primary.ID() is not None and not suffixes:
            name = primary.ID().getText()
            var = self.resolve_variable(name)
            return LValue(kind="var", var=var, type_name=var.type_name)

        if primary.ID() is not None:
            var = self.resolve_variable(primary.ID().getText())
            self.emit_load_var(var)
            current_type = var.type_name
        else:
            current_type = self.gen_primary(primary)

        for index, suffix in enumerate(suffixes):
            is_last = index == len(suffixes) - 1

            if suffix.DOT() is not None and suffix.LPAREN() is None:
                field_name = suffix.ID().getText()
                field_info = self.classes[current_type].fields[field_name]

                if is_last:
                    return LValue(
                        kind="field",
                        type_name=field_info.type_name,
                        owner_type=current_type,
                        field_name=field_name,
                    )

                self.writer.emit(
                    f"getfield {current_type}/{field_name} {field_info.descriptor}"
                )
                current_type = field_info.type_name

            elif suffix.LBRACK() is not None:
                if not is_array_type(current_type):
                    raise NotImplementedError("Indexacao em variavel nao vetor no back-end.")

                element_type = array_element_type(current_type)
                index_expr = self.find_child_by_type_name(suffix, "ExpressionContext")
                if index_expr is None:
                    raise NotImplementedError("Indice de vetor nao encontrado no back-end.")

                self.gen_expression(index_expr)

                if is_last:
                    return LValue(kind="array", var=None, type_name=element_type)

                self.writer.emit(jasmin_array_load_instruction(element_type))
                current_type = element_type

            else:
                raise NotImplementedError(
                    "Back-end Jasmin ainda suporta atribuicao apenas em variaveis simples, elementos de vetor ou atributos."
                )

        raise NotImplementedError(
            "Back-end Jasmin ainda suporta atribuicao apenas em variaveis simples, elementos de vetor ou atributos."
        )

    def emit_store_lvalue(self, target: LValue):
        if target.kind == "var":
            self.emit_store_var(target.var)
        elif target.kind == "array":
            self.writer.emit(jasmin_array_store_instruction(target.type_name))
        elif target.kind == "field":
            desc = jasmin_descriptor(target.type_name)
            self.writer.emit(f"putfield {target.owner_type}/{target.field_name} {desc}")
        else:
            raise NotImplementedError(
                "Destino de atribuicao nao suportado no back-end."
            )

    def emit_load_lvalue_value(self, target: LValue):
        """
        Carrega o valor atual de um destino de atribuicao.

        Importante:
        - Para variavel simples, apenas carrega a variavel.
        - Para vetor, resolve_lvalue ja deixou arrayref e indice na pilha.
        Entao duplicamos arrayref/indice antes de usar xaload.
        - Para atributo, resolve_lvalue ja deixou objectref na pilha.
        Entao duplicamos objectref antes de usar getfield.
        """
        if target.kind == "var":
            self.emit_load_var(target.var)

        elif target.kind == "array":
            self.writer.emit("dup2")
            self.writer.emit(jasmin_array_load_instruction(target.type_name))

        elif target.kind == "field":
            desc = jasmin_descriptor(target.type_name)
            self.writer.emit("dup")
            self.writer.emit(f"getfield {target.owner_type}/{target.field_name} {desc}")

        else:
            raise NotImplementedError("Destino de leitura nao suportado no back-end.")

    def allocate_temp_slot(self, type_name: str) -> int:
        """
        Reserva um slot temporario para conversoes internas do back-end.

        Em metodos normais, usa os slots locais do metodo atual.
        Em <clinit>, quando current_method e None, usa slot 0.
        """
        if self.current_method is None:
            return 0

        slot = self.current_method.next_slot

        if type_name == "real":
            self.current_method.next_slot += 2
        else:
            self.current_method.next_slot += 1

        return slot

    def prepare_numeric_binary_operands(self, left_type: str, right_type: str) -> str:
        """
        Ajusta a pilha para operacoes numericas binarias.

        Casos:
        - int + int: fica como int
        - real + real: fica como real
        - real + int: converte o int do topo com i2d
        - int + real: guarda o real temporariamente, converte o int que ficou abaixo e recarrega o real
        """
        if left_type == "real" and right_type == "real":
            return "real"

        if left_type == "int" and right_type == "int":
            return "int"

        if left_type == "real" and right_type == "int":
            self.writer.emit("i2d")
            return "real"

        if left_type == "int" and right_type == "real":
            temp_slot = self.allocate_temp_slot("real")
            self.writer.emit(f"dstore {temp_slot}")
            self.writer.emit("i2d")
            self.writer.emit(f"dload {temp_slot}")
            return "real"

        raise NotImplementedError(
            f"Operacao numerica nao suportada entre {left_type} e {right_type}."
        )

    def emit_numeric_operation(self, op: str, type_name: str):
        if type_name == "real":
            if op == "+":
                self.writer.emit("dadd")
            elif op == "-":
                self.writer.emit("dsub")
            elif op == "*":
                self.writer.emit("dmul")
            elif op == "/":
                self.writer.emit("ddiv")
            else:
                raise NotImplementedError(f"Operador {op} nao suportado para real.")
            return

        if type_name == "int":
            if op == "+":
                self.writer.emit("iadd")
            elif op == "-":
                self.writer.emit("isub")
            elif op == "*":
                self.writer.emit("imul")
            elif op == "/":
                self.writer.emit("idiv")
            elif op == "%":
                self.writer.emit("irem")
            else:
                raise NotImplementedError(f"Operador {op} nao suportado para int.")
            return

        raise NotImplementedError(
            f"Operacao numerica nao suportada para tipo {type_name}."
        )

    def emit_value_to_string(self, type_name: str):
        desc = jasmin_descriptor(type_name)
        self.writer.emit(f"invokestatic java/lang/String/valueOf({desc})Ljava/lang/String;")

    def emit_string_concat(self, left_type: str, right_type: str):
        if left_type != "str" and right_type != "str":
            raise NotImplementedError("Concatenacao exige pelo menos um operando str.")

        if left_type == "str" and right_type == "str":
            pass
        elif left_type == "str":
            self.emit_value_to_string(right_type)
        elif right_type == "str":
            temp_slot = self.allocate_temp_slot("str")
            self.writer.emit(f"astore {temp_slot}")
            self.emit_value_to_string(left_type)
            self.writer.emit(f"aload {temp_slot}")

        self.writer.emit(
            "invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;"
        )

    def emit_compound_operation(self, op: str, type_name: str):
        if type_name == "bool" and op in {"&&=", "||="}:
            self.writer.emit("iand" if op == "&&=" else "ior")
            return

        if type_name == "real":
            if op == "+=":
                self.writer.emit("dadd")
            elif op == "-=":
                self.writer.emit("dsub")
            elif op == "*=":
                self.writer.emit("dmul")
            elif op == "/=":
                self.writer.emit("ddiv")
            else:
                raise NotImplementedError(
                    "Operadores %= e **= nao sao suportados para real no back-end."
                )
            return

        if type_name == "int":
            if op == "+=":
                self.writer.emit("iadd")
            elif op == "-=":
                self.writer.emit("isub")
            elif op == "*=":
                self.writer.emit("imul")
            elif op == "/=":
                self.writer.emit("idiv")
            elif op == "%=":
                self.writer.emit("irem")
            elif op == "**=":
                temp_slot = self.allocate_temp_slot("int")
                self.writer.emit(f"istore {temp_slot}")
                self.writer.emit("i2d")
                self.writer.emit(f"iload {temp_slot}")
                self.writer.emit("i2d")
                self.writer.emit("invokestatic java/lang/Math/pow(DD)D")
                self.writer.emit("d2i")
            return

        raise NotImplementedError(
            f"Operador composto {op} nao suportado para tipo {type_name}."
        )

    def emit_load_var(self, var: VarInfo):
        if var.is_global:
            self.writer.emit(f"getstatic {self.class_name}/{var.name} {var.descriptor}")
            return

        if var.type_name in {"int", "bool"}:
            self.writer.emit(f"iload {var.slot}")
        elif var.type_name == "real":
            self.writer.emit(f"dload {var.slot}")
        else:
            self.writer.emit(f"aload {var.slot}")

    def emit_store_var(self, var: VarInfo):
        if var.is_global:
            self.writer.emit(f"putstatic {self.class_name}/{var.name} {var.descriptor}")
            return

        if var.type_name in {"int", "bool"}:
            self.writer.emit(f"istore {var.slot}")
        elif var.type_name == "real":
            self.writer.emit(f"dstore {var.slot}")
        else:
            self.writer.emit(f"astore {var.slot}")

    def emit_default_value(self, type_name: str):
        if type_name in {"int", "bool"}:
            self.writer.emit("iconst_0")
        elif type_name == "real":
            self.writer.emit("dconst_0")
        elif type_name == "str":
            self.writer.emit('ldc ""')
        else:
            self.writer.emit("aconst_null")

    def emit_push_int(self, value: int):
        if -1 <= value <= 5:
            if value == -1:
                self.writer.emit("iconst_m1")
            else:
                self.writer.emit(f"iconst_{value}")
        elif -128 <= value <= 127:
            self.writer.emit(f"bipush {value}")
        elif -32768 <= value <= 32767:
            self.writer.emit(f"sipush {value}")
        else:
            self.writer.emit(f"ldc {value}")

    def emit_pop_if_needed(self, type_name: str):
        if type_name == "void":
            return
        if type_name == "real":
            self.writer.emit("pop2")
        else:
            self.writer.emit("pop")

    def emit_new_array(self, base_type: str, size: int):
        self.emit_push_int(size)
        self.writer.emit(jasmin_newarray_instruction(base_type))

    def emit_new_array_from_sizes(self, type_name: str, sizes: list[int]):
        if not sizes:
            raise NotImplementedError("Vetor sem tamanho nao suportado no back-end.")

        element_type = array_element_type(type_name)
        self.emit_new_array(element_type, sizes[0])

        # Para vetores multidimensionais, aloca cada subvetor.
        # Ex.: int[3][3] vira um array de 3 referencias para int[3].
        if len(sizes) > 1:
            for index in range(sizes[0]):
                self.writer.emit("dup")
                self.emit_push_int(index)
                self.emit_new_array_from_sizes(element_type, sizes[1:])
                self.writer.emit("aastore")

    def find_array_literal(self, initializer_ctx):
        if initializer_ctx is None:
            return None

        return self.find_child_by_type_name(initializer_ctx, "ArrayLiteralContext")

    def emit_array_creation_with_initializer(
        self, type_name: str, array_sizes, initializer_ctx
    ):
        if isinstance(array_sizes, int):
            sizes = [array_sizes]
        else:
            sizes = list(array_sizes or [])

        base_type = array_element_type(type_name)
        self.emit_new_array_from_sizes(type_name, sizes)

        array_literal = self.find_array_literal(initializer_ctx)

        if array_literal is None:
            return

        if len(sizes) != 1:
            raise NotImplementedError(
                "Inicializacao literal de vetor multidimensional ainda nao suportada no back-end."
            )

        expressions = array_literal.expression()

        for index, expr in enumerate(expressions):
            self.writer.emit("dup")
            self.emit_push_int(index)

            expr_type = self.gen_expression(expr)

            if base_type == "real" and expr_type == "int":
                self.writer.emit("i2d")

            self.writer.emit(jasmin_array_store_instruction(base_type))

    # ======================================================
    # Busca auxiliar na parse tree
    # ======================================================

    def find_child_by_type_name(self, ctx, type_name: str):
        if type(ctx).__name__ == type_name:
            return ctx

        if not hasattr(ctx, "getChildCount"):
            return None

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            found = self.find_child_by_type_name(child, type_name)

            if found is not None:
                return found

        return None

    def find_children_by_type_name(self, ctx, type_name: str) -> list:
        found_nodes = []

        if type(ctx).__name__ == type_name:
            found_nodes.append(ctx)

        if not hasattr(ctx, "getChildCount"):
            return found_nodes

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            found_nodes.extend(self.find_children_by_type_name(child, type_name))

        return found_nodes

    # ======================================================
    # Comparacoes e auxiliares
    # ======================================================

    def emit_comparison(self, left_type: str, right_type: str, op: str):
        true_label = self.labels.new("cmp_true")
        end_label = self.labels.new("cmp_end")

        if left_type in {"int", "real"} and right_type in {"int", "real"}:
            numeric_type = self.prepare_numeric_binary_operands(left_type, right_type)

            if numeric_type == "real":
                self.writer.emit("dcmpg")
                instruction = {
                    "==": "ifeq",
                    "!=": "ifne",
                    ">": "ifgt",
                    ">=": "ifge",
                    "<": "iflt",
                    "<=": "ifle",
                }[op]
                self.writer.emit(f"{instruction} {true_label}")
            else:
                instruction = {
                    "==": "if_icmpeq",
                    "!=": "if_icmpne",
                    ">": "if_icmpgt",
                    ">=": "if_icmpge",
                    "<": "if_icmplt",
                    "<=": "if_icmple",
                }[op]
                self.writer.emit(f"{instruction} {true_label}")

        else:
            instruction = {
                "==": "if_icmpeq",
                "!=": "if_icmpne",
                ">": "if_icmpgt",
                ">=": "if_icmpge",
                "<": "if_icmplt",
                "<=": "if_icmple",
            }[op]
            self.writer.emit(f"{instruction} {true_label}")

        self.writer.emit("iconst_0")
        self.writer.emit(f"goto {end_label}")
        self.writer.emit_label(true_label)
        self.writer.emit("iconst_1")
        self.writer.emit_label(end_label)

    def emit_real_to_bool(self):
        true_label = self.labels.new("bool_true")
        end_label = self.labels.new("bool_end")

        self.writer.emit("dconst_0")
        self.writer.emit("dcmpg")
        self.writer.emit(f"ifne {true_label}")
        self.writer.emit("iconst_0")
        self.writer.emit(f"goto {end_label}")
        self.writer.emit_label(true_label)
        self.writer.emit("iconst_1")
        self.writer.emit_label(end_label)

    def emit_int_to_bool(self):
        true_label = self.labels.new("bool_true")
        end_label = self.labels.new("bool_end")

        self.writer.emit(f"ifne {true_label}")
        self.writer.emit("iconst_0")
        self.writer.emit(f"goto {end_label}")
        self.writer.emit_label(true_label)
        self.writer.emit("iconst_1")
        self.writer.emit_label(end_label)
