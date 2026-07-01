lexer grammar JSSLexer;

// =====================
// Palavras reservadas
// =====================

LET         : 'let';
CONST       : 'const';
FUNCTION    : 'function';
VOID        : 'void';
CLASS       : 'class';
CONSTRUCTOR : 'constructor';
THIS        : 'this';
NEW         : 'new';

IF          : 'if';
ELSE        : 'else';
WHILE       : 'while';
FOR         : 'for';
BREAK       : 'break';
RETURN      : 'return';

TRUE        : 'true';
FALSE       : 'false';
NULL        : 'null';

INPUT       : 'input';
CONSOLE_LOG : 'console.log';

INT_TYPE    : 'int';
REAL_TYPE   : 'real';
STR_TYPE    : 'str';
BOOL_TYPE   : 'bool';

// =====================
// Operadores compostos
// =====================

POW_ASSIGN   : '**=';
AND_ASSIGN   : '&&=';
OR_ASSIGN    : '||=';
PLUS_ASSIGN  : '+=';
MINUS_ASSIGN : '-=';
MULT_ASSIGN  : '*=';
DIV_ASSIGN   : '/=';
MOD_ASSIGN   : '%=';

EQ_EQ        : '==';
NEQ          : '!=';
GE           : '>=';
LE           : '<=';
AND          : '&&';
OR           : '||';
INC          : '++';
DEC          : '--';
POW          : '**';

// =====================
// Operadores simples
// =====================

ASSIGN : '=';
GT     : '>';
LT     : '<';
NOT    : '!';
PLUS   : '+';
MINUS  : '-';
MULT   : '*';
DIV    : '/';
MOD    : '%';

// =====================
// Delimitadores
// =====================

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
SEMI   : ';';
COMMA  : ',';
DOT    : '.';

// =====================
// Literais
// =====================

REAL_LITERAL
    : DIGIT+ '.' DIGIT* EXPONENT?
    | '.' DIGIT+ EXPONENT?
    | DIGIT+ EXPONENT
    ;

INT_LITERAL
    : DIGIT+
    ;

STRING_LITERAL
    : '"' ( ESC_SEQ | ~["\\\r\n] )* '"'
    ;

// =====================
// Identificadores
// =====================

ID
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// =====================
// Comentários e espaços
// =====================

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

// =====================
// Fragmentos auxiliares
// =====================

fragment DIGIT
    : [0-9]
    ;

fragment EXPONENT
    : [eE] [+-]? DIGIT+
    ;

fragment ESC_SEQ
    : '\\' [btnr"\\]
    ;