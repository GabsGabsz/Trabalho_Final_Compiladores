# Generated from grammar/JSSParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JSSParser import JSSParser
else:
    from JSSParser import JSSParser

# This class defines a complete listener for a parse tree produced by JSSParser.
class JSSParserListener(ParseTreeListener):

    # Enter a parse tree produced by JSSParser#program.
    def enterProgram(self, ctx:JSSParser.ProgramContext):
        pass

    # Exit a parse tree produced by JSSParser#program.
    def exitProgram(self, ctx:JSSParser.ProgramContext):
        pass


    # Enter a parse tree produced by JSSParser#topLevelDeclaration.
    def enterTopLevelDeclaration(self, ctx:JSSParser.TopLevelDeclarationContext):
        pass

    # Exit a parse tree produced by JSSParser#topLevelDeclaration.
    def exitTopLevelDeclaration(self, ctx:JSSParser.TopLevelDeclarationContext):
        pass


    # Enter a parse tree produced by JSSParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:JSSParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by JSSParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:JSSParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by JSSParser#variableModifier.
    def enterVariableModifier(self, ctx:JSSParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by JSSParser#variableModifier.
    def exitVariableModifier(self, ctx:JSSParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by JSSParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:JSSParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by JSSParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:JSSParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by JSSParser#initializer.
    def enterInitializer(self, ctx:JSSParser.InitializerContext):
        pass

    # Exit a parse tree produced by JSSParser#initializer.
    def exitInitializer(self, ctx:JSSParser.InitializerContext):
        pass


    # Enter a parse tree produced by JSSParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:JSSParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by JSSParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:JSSParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by JSSParser#type.
    def enterType(self, ctx:JSSParser.TypeContext):
        pass

    # Exit a parse tree produced by JSSParser#type.
    def exitType(self, ctx:JSSParser.TypeContext):
        pass


    # Enter a parse tree produced by JSSParser#baseType.
    def enterBaseType(self, ctx:JSSParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by JSSParser#baseType.
    def exitBaseType(self, ctx:JSSParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by JSSParser#primitiveType.
    def enterPrimitiveType(self, ctx:JSSParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by JSSParser#primitiveType.
    def exitPrimitiveType(self, ctx:JSSParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by JSSParser#arraySuffix.
    def enterArraySuffix(self, ctx:JSSParser.ArraySuffixContext):
        pass

    # Exit a parse tree produced by JSSParser#arraySuffix.
    def exitArraySuffix(self, ctx:JSSParser.ArraySuffixContext):
        pass


    # Enter a parse tree produced by JSSParser#returnType.
    def enterReturnType(self, ctx:JSSParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by JSSParser#returnType.
    def exitReturnType(self, ctx:JSSParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by JSSParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JSSParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by JSSParser#classDeclaration.
    def exitClassDeclaration(self, ctx:JSSParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by JSSParser#classMember.
    def enterClassMember(self, ctx:JSSParser.ClassMemberContext):
        pass

    # Exit a parse tree produced by JSSParser#classMember.
    def exitClassMember(self, ctx:JSSParser.ClassMemberContext):
        pass


    # Enter a parse tree produced by JSSParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:JSSParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by JSSParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:JSSParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by JSSParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:JSSParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by JSSParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:JSSParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by JSSParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:JSSParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by JSSParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:JSSParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by JSSParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:JSSParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by JSSParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:JSSParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by JSSParser#parameterList.
    def enterParameterList(self, ctx:JSSParser.ParameterListContext):
        pass

    # Exit a parse tree produced by JSSParser#parameterList.
    def exitParameterList(self, ctx:JSSParser.ParameterListContext):
        pass


    # Enter a parse tree produced by JSSParser#parameter.
    def enterParameter(self, ctx:JSSParser.ParameterContext):
        pass

    # Exit a parse tree produced by JSSParser#parameter.
    def exitParameter(self, ctx:JSSParser.ParameterContext):
        pass


    # Enter a parse tree produced by JSSParser#block.
    def enterBlock(self, ctx:JSSParser.BlockContext):
        pass

    # Exit a parse tree produced by JSSParser#block.
    def exitBlock(self, ctx:JSSParser.BlockContext):
        pass


    # Enter a parse tree produced by JSSParser#statement.
    def enterStatement(self, ctx:JSSParser.StatementContext):
        pass

    # Exit a parse tree produced by JSSParser#statement.
    def exitStatement(self, ctx:JSSParser.StatementContext):
        pass


    # Enter a parse tree produced by JSSParser#ifStatement.
    def enterIfStatement(self, ctx:JSSParser.IfStatementContext):
        pass

    # Exit a parse tree produced by JSSParser#ifStatement.
    def exitIfStatement(self, ctx:JSSParser.IfStatementContext):
        pass


    # Enter a parse tree produced by JSSParser#elseIfBlock.
    def enterElseIfBlock(self, ctx:JSSParser.ElseIfBlockContext):
        pass

    # Exit a parse tree produced by JSSParser#elseIfBlock.
    def exitElseIfBlock(self, ctx:JSSParser.ElseIfBlockContext):
        pass


    # Enter a parse tree produced by JSSParser#elseBlock.
    def enterElseBlock(self, ctx:JSSParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by JSSParser#elseBlock.
    def exitElseBlock(self, ctx:JSSParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by JSSParser#whileStatement.
    def enterWhileStatement(self, ctx:JSSParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by JSSParser#whileStatement.
    def exitWhileStatement(self, ctx:JSSParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by JSSParser#forStatement.
    def enterForStatement(self, ctx:JSSParser.ForStatementContext):
        pass

    # Exit a parse tree produced by JSSParser#forStatement.
    def exitForStatement(self, ctx:JSSParser.ForStatementContext):
        pass


    # Enter a parse tree produced by JSSParser#forInit.
    def enterForInit(self, ctx:JSSParser.ForInitContext):
        pass

    # Exit a parse tree produced by JSSParser#forInit.
    def exitForInit(self, ctx:JSSParser.ForInitContext):
        pass


    # Enter a parse tree produced by JSSParser#forCondition.
    def enterForCondition(self, ctx:JSSParser.ForConditionContext):
        pass

    # Exit a parse tree produced by JSSParser#forCondition.
    def exitForCondition(self, ctx:JSSParser.ForConditionContext):
        pass


    # Enter a parse tree produced by JSSParser#forUpdate.
    def enterForUpdate(self, ctx:JSSParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by JSSParser#forUpdate.
    def exitForUpdate(self, ctx:JSSParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by JSSParser#expressionList.
    def enterExpressionList(self, ctx:JSSParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by JSSParser#expressionList.
    def exitExpressionList(self, ctx:JSSParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by JSSParser#breakStatement.
    def enterBreakStatement(self, ctx:JSSParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by JSSParser#breakStatement.
    def exitBreakStatement(self, ctx:JSSParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by JSSParser#returnStatement.
    def enterReturnStatement(self, ctx:JSSParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by JSSParser#returnStatement.
    def exitReturnStatement(self, ctx:JSSParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by JSSParser#inputStatement.
    def enterInputStatement(self, ctx:JSSParser.InputStatementContext):
        pass

    # Exit a parse tree produced by JSSParser#inputStatement.
    def exitInputStatement(self, ctx:JSSParser.InputStatementContext):
        pass


    # Enter a parse tree produced by JSSParser#inputArgumentList.
    def enterInputArgumentList(self, ctx:JSSParser.InputArgumentListContext):
        pass

    # Exit a parse tree produced by JSSParser#inputArgumentList.
    def exitInputArgumentList(self, ctx:JSSParser.InputArgumentListContext):
        pass


    # Enter a parse tree produced by JSSParser#inputArgument.
    def enterInputArgument(self, ctx:JSSParser.InputArgumentContext):
        pass

    # Exit a parse tree produced by JSSParser#inputArgument.
    def exitInputArgument(self, ctx:JSSParser.InputArgumentContext):
        pass


    # Enter a parse tree produced by JSSParser#consoleLogStatement.
    def enterConsoleLogStatement(self, ctx:JSSParser.ConsoleLogStatementContext):
        pass

    # Exit a parse tree produced by JSSParser#consoleLogStatement.
    def exitConsoleLogStatement(self, ctx:JSSParser.ConsoleLogStatementContext):
        pass


    # Enter a parse tree produced by JSSParser#expression.
    def enterExpression(self, ctx:JSSParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#expression.
    def exitExpression(self, ctx:JSSParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:JSSParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:JSSParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:JSSParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by JSSParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:JSSParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by JSSParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:JSSParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:JSSParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:JSSParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:JSSParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#equalityExpression.
    def enterEqualityExpression(self, ctx:JSSParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#equalityExpression.
    def exitEqualityExpression(self, ctx:JSSParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#relationalExpression.
    def enterRelationalExpression(self, ctx:JSSParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#relationalExpression.
    def exitRelationalExpression(self, ctx:JSSParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:JSSParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:JSSParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:JSSParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:JSSParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#powerExpression.
    def enterPowerExpression(self, ctx:JSSParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#powerExpression.
    def exitPowerExpression(self, ctx:JSSParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#unaryExpression.
    def enterUnaryExpression(self, ctx:JSSParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#unaryExpression.
    def exitUnaryExpression(self, ctx:JSSParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#postfixExpression.
    def enterPostfixExpression(self, ctx:JSSParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#postfixExpression.
    def exitPostfixExpression(self, ctx:JSSParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#postfixSuffix.
    def enterPostfixSuffix(self, ctx:JSSParser.PostfixSuffixContext):
        pass

    # Exit a parse tree produced by JSSParser#postfixSuffix.
    def exitPostfixSuffix(self, ctx:JSSParser.PostfixSuffixContext):
        pass


    # Enter a parse tree produced by JSSParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:JSSParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:JSSParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#newExpression.
    def enterNewExpression(self, ctx:JSSParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#newExpression.
    def exitNewExpression(self, ctx:JSSParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#castExpression.
    def enterCastExpression(self, ctx:JSSParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by JSSParser#castExpression.
    def exitCastExpression(self, ctx:JSSParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by JSSParser#argumentList.
    def enterArgumentList(self, ctx:JSSParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by JSSParser#argumentList.
    def exitArgumentList(self, ctx:JSSParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by JSSParser#literal.
    def enterLiteral(self, ctx:JSSParser.LiteralContext):
        pass

    # Exit a parse tree produced by JSSParser#literal.
    def exitLiteral(self, ctx:JSSParser.LiteralContext):
        pass



del JSSParser