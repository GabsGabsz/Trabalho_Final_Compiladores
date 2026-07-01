from dataclasses import dataclass, field

from semantic.types import JssType

@dataclass
class Symbol:
    name: str
    type: JssType
    kind: str
    line: int
    column: int
    is_const: bool = False
    params: list[tuple[str, JssType]] = field(default_factory=list)
    return_type: JssType | None = None
    fields: dict[str, "Symbol"] = field(default_factory=dict)
    methods: dict[str, "Symbol"] = field(default_factory=dict)
    constructor_params: list[tuple[str, JssType]] = field(default_factory=list)

    def signature(self) -> str:
        if self.kind in {"function", "method"}:
            params = ", ".join(str(t) for _, t in self.params)
            return f"{self.name}({params}) -> {self.return_type}"
        return f"{self.name}: {self.type}"