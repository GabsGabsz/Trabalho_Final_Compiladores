from errors.compiler_error import CompilerError
from semantic.symbols import Symbol


class Scope:
    def __init__(self, name: str, parent: "Scope | None" = None):
        self.name = name
        self.parent = parent
        self.symbols: dict[str, Symbol] = {}

    def define(self, symbol: Symbol):
        if symbol.name in self.symbols:
            previous = self.symbols[symbol.name]
            raise CompilerError(
                phase="SEMANTICO",
                line=symbol.line,
                column=symbol.column,
                message=(
                    f"identificador '{symbol.name}' ja declarado neste escopo "
                    f"na linha {previous.line}."
                )
            )

        self.symbols[symbol.name] = symbol

    def resolve_local(self, name: str) -> Symbol | None:
        return self.symbols.get(name)

    def resolve(self, name: str) -> Symbol | None:
        current: Scope | None = self

        while current is not None:
            symbol = current.resolve_local(name)
            if symbol is not None:
                return symbol
            current = current.parent

        return None


class ScopeStack:
    def __init__(self):
        self.global_scope = Scope("global")
        self.current_scope = self.global_scope

    def enter(self, name: str):
        self.current_scope = Scope(name, self.current_scope)

    def exit(self):
        if self.current_scope.parent is not None:
            self.current_scope = self.current_scope.parent

    def define(self, symbol: Symbol):
        self.current_scope.define(symbol)

    def resolve(self, name: str) -> Symbol | None:
        return self.current_scope.resolve(name)

    def resolve_global(self, name: str) -> Symbol | None:
        return self.global_scope.resolve_local(name)