parser grammar JSSParser;

options {
    tokenVocab = JSSLexer;
}

// =====================
// Programa
// =====================

program
    : topLevelDeclaration* EOF
    ;

topLevelDeclaration
    : classDeclaration
    | functionDeclaration
    | statement
    ;

// =====================
// Declarações de variáveis
// =====================

variableDeclaration
    : variableModifier type variableDeclarator (COMMA variableDeclarator)*
    ;

variableModifier
    : LET
    | CONST
    ;

variableDeclarator
    : ID (ASSIGN initializer)?
    ;

initializer
    : expression
    | arrayLiteral
    ;

arrayLiteral
    : LBRACK (expression (COMMA expression)*)? RBRACK
    ;

// =====================
// Tipos
// =====================

type
    : baseType arraySuffix?
    ;

baseType
    : primitiveType
    | ID
    ;

primitiveType
    : INT_TYPE
    | REAL_TYPE
    | STR_TYPE
    | BOOL_TYPE
    ;

arraySuffix
    : (LBRACK INT_LITERAL RBRACK)+
    ;

returnType
    : type
    | VOID
    ;

// =====================
// Classes
// =====================

classDeclaration
    : CLASS ID LBRACE classMember* RBRACE
    ;

classMember
    : fieldDeclaration
    | constructorDeclaration
    | methodDeclaration
    ;

fieldDeclaration
    : type ID SEMI
    ;

constructorDeclaration
    : ID CONSTRUCTOR LPAREN parameterList? RPAREN block
    ;

methodDeclaration
    : returnType ID LPAREN parameterList? RPAREN block
    ;

// =====================
// Funções
// =====================

functionDeclaration
    : FUNCTION returnType ID LPAREN parameterList? RPAREN block
    ;

parameterList
    : parameter (COMMA parameter)*
    ;

parameter
    : type ID
    ;

// =====================
// Blocos e comandos
// =====================

block
    : LBRACE statement* RBRACE
    ;

statement
    : block
    | variableDeclaration SEMI
    | ifStatement
    | whileStatement
    | forStatement
    | breakStatement SEMI
    | returnStatement SEMI
    | inputStatement SEMI
    | consoleLogStatement SEMI
    | expression SEMI
    | SEMI
    ;

ifStatement
    : IF LPAREN expression RPAREN block elseIfBlock* elseBlock?
    ;

elseIfBlock
    : ELSE IF LPAREN expression RPAREN block
    ;

elseBlock
    : ELSE block
    ;

whileStatement
    : WHILE LPAREN expression RPAREN block
    ;

forStatement
    : FOR LPAREN forInit? SEMI forCondition? SEMI forUpdate? RPAREN block
    ;

forInit
    : variableDeclaration
    | expressionList
    ;

forCondition
    : expression
    ;

forUpdate
    : expressionList
    ;

expressionList
    : expression (COMMA expression)*
    ;

breakStatement
    : BREAK
    ;

returnStatement
    : RETURN expression?
    ;

inputStatement
    : INPUT LPAREN inputArgumentList? RPAREN
    ;

inputArgumentList
    : inputArgument (COMMA inputArgument)*
    ;

inputArgument
    : postfixExpression
    ;

consoleLogStatement
    : CONSOLE_LOG LPAREN argumentList? RPAREN
    ;

// =====================
// Expressões
// =====================

expression
    : assignmentExpression
    ;

assignmentExpression
    : postfixExpression assignmentOperator assignmentExpression
    | logicalOrExpression
    ;

assignmentOperator
    : ASSIGN
    | PLUS_ASSIGN
    | MINUS_ASSIGN
    | MULT_ASSIGN
    | DIV_ASSIGN
    | MOD_ASSIGN
    | POW_ASSIGN
    | AND_ASSIGN
    | OR_ASSIGN
    ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : equalityExpression (AND equalityExpression)*
    ;

equalityExpression
    : relationalExpression ((EQ_EQ | NEQ) relationalExpression)*
    ;

relationalExpression
    : additiveExpression ((GT | GE | LT | LE) additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : powerExpression ((MULT | DIV | MOD) powerExpression)*
    ;

powerExpression
    : unaryExpression (POW powerExpression)?
    ;

unaryExpression
    : (NOT | PLUS | MINUS | INC | DEC) unaryExpression
    | postfixExpression
    ;

postfixExpression
    : primaryExpression postfixSuffix*
    ;

postfixSuffix
    : DOT ID LPAREN argumentList? RPAREN
    | LBRACK expression RBRACK
    | DOT ID
    | LPAREN argumentList? RPAREN
    | INC
    | DEC
    ;
    
primaryExpression
    : literal
    | ID
    | THIS
    | newExpression
    | castExpression
    | LPAREN expression RPAREN
    ;

newExpression
    : NEW ID LPAREN argumentList? RPAREN
    ;

castExpression
    : primitiveType LPAREN expression RPAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;

literal
    : INT_LITERAL
    | REAL_LITERAL
    | STRING_LITERAL
    | TRUE
    | FALSE
    | NULL
    ;