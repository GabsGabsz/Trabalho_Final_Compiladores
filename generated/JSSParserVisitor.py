# Generated from grammar/JSSParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JSSParser import JSSParser
else:
    from JSSParser import JSSParser

# This class defines a complete generic visitor for a parse tree produced by JSSParser.

class JSSParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JSSParser#program.
    def visitProgram(self, ctx:JSSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#topLevelDeclaration.
    def visitTopLevelDeclaration(self, ctx:JSSParser.TopLevelDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:JSSParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#variableModifier.
    def visitVariableModifier(self, ctx:JSSParser.VariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:JSSParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#initializer.
    def visitInitializer(self, ctx:JSSParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:JSSParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#type.
    def visitType(self, ctx:JSSParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#baseType.
    def visitBaseType(self, ctx:JSSParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#primitiveType.
    def visitPrimitiveType(self, ctx:JSSParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#arraySuffix.
    def visitArraySuffix(self, ctx:JSSParser.ArraySuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#returnType.
    def visitReturnType(self, ctx:JSSParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JSSParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#classMember.
    def visitClassMember(self, ctx:JSSParser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:JSSParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:JSSParser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:JSSParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:JSSParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#parameterList.
    def visitParameterList(self, ctx:JSSParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#parameter.
    def visitParameter(self, ctx:JSSParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#block.
    def visitBlock(self, ctx:JSSParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#statement.
    def visitStatement(self, ctx:JSSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#ifStatement.
    def visitIfStatement(self, ctx:JSSParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#elseIfBlock.
    def visitElseIfBlock(self, ctx:JSSParser.ElseIfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#elseBlock.
    def visitElseBlock(self, ctx:JSSParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#whileStatement.
    def visitWhileStatement(self, ctx:JSSParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#forStatement.
    def visitForStatement(self, ctx:JSSParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#forInit.
    def visitForInit(self, ctx:JSSParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#breakStatement.
    def visitBreakStatement(self, ctx:JSSParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#returnStatement.
    def visitReturnStatement(self, ctx:JSSParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#inputStatement.
    def visitInputStatement(self, ctx:JSSParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#inputArgumentList.
    def visitInputArgumentList(self, ctx:JSSParser.InputArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#inputArgument.
    def visitInputArgument(self, ctx:JSSParser.InputArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#consoleLogStatement.
    def visitConsoleLogStatement(self, ctx:JSSParser.ConsoleLogStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#expression.
    def visitExpression(self, ctx:JSSParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:JSSParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:JSSParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:JSSParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:JSSParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#equalityExpression.
    def visitEqualityExpression(self, ctx:JSSParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#relationalExpression.
    def visitRelationalExpression(self, ctx:JSSParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:JSSParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:JSSParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#powerExpression.
    def visitPowerExpression(self, ctx:JSSParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#unaryExpression.
    def visitUnaryExpression(self, ctx:JSSParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#postfixExpression.
    def visitPostfixExpression(self, ctx:JSSParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#postfixSuffix.
    def visitPostfixSuffix(self, ctx:JSSParser.PostfixSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:JSSParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#newExpression.
    def visitNewExpression(self, ctx:JSSParser.NewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#castExpression.
    def visitCastExpression(self, ctx:JSSParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#argumentList.
    def visitArgumentList(self, ctx:JSSParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#literal.
    def visitLiteral(self, ctx:JSSParser.LiteralContext):
        return self.visitChildren(ctx)



del JSSParser