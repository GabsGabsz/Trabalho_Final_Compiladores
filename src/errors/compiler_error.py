class CompilerError(Exception):
    """
    Erro padronizado do compilador JSS.
    """

    def __init__(self, phase: str, line: int, column: int, message: str):
        self.phase = phase
        self.line = line
        self.column = column
        self.message = message
        super().__init__(self.__str__())

    def __str__(self) -> str:
        return (
            f"ERRO {self.phase} na linha {self.line}, "
            f"coluna {self.column}: {self.message}"
        )