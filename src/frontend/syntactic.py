from JSSParser import JSSParser

from errors.error_listener import JSSParserErrorListener

class SyntacticAnalyzer:
    """
    Etapa de análise sintática.

    Recebe o fluxo de tokens e verifica se ele respeita a gramática JSS.
    """
    
    def analyze(self, token_stream):
        parser = JSSParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(JSSParserErrorListener())
        parser.buildParseTrees = True

        tree = parser.program()

        return tree, parser