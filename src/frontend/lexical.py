from antlr4 import InputStream, CommonTokenStream

from JSSLexer import JSSLexer
from errors.error_listener import JSSLexerErrorListener


class LexicalAnalyzer:
    """
    Etapa de análise léxica.

    Recebe o código-fonte em texto puro e transforma em fluxo de tokens.
    """

    def analyze(self, source_code: str) -> CommonTokenStream:
        input_stream = InputStream(source_code)

        lexer = JSSLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(JSSLexerErrorListener())

        token_stream = CommonTokenStream(lexer)

        # Força o lexer a ler todos os tokens agora.
        # Assim, erro léxico aparece antes do parser começar.
        token_stream.fill()
        token_stream.seek(0)

        return token_stream