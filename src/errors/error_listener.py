from antlr4.error.ErrorListener import ErrorListener

from errors.compiler_error import CompilerError


class JSSLexerErrorListener(ErrorListener):
    """
    Captura erros léxicos gerados pelo lexer do ANTLR.
    """

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise CompilerError(
            phase="LEXICO",
            line=line,
            column=column + 1,
            message=msg
        )


class JSSParserErrorListener(ErrorListener):
    """
    Captura erros sintáticos gerados pelo parser do ANTLR.
    """

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise CompilerError(
            phase="SINTATICO",
            line=line,
            column=column + 1,
            message=msg
        )