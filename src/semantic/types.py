from dataclasses import dataclass, field

@dataclass(frozen=True)
class JssType:
    name: str
    is_array: bool = False
    array_size: int | None = None
    dimensions: tuple[int, ...] = field(default_factory=tuple)

    def __post_init__(self):
        if self.is_array and not self.dimensions and self.array_size is not None:
            object.__setattr__(self, "dimensions", (self.array_size,))
        if self.dimensions and not self.is_array:
            object.__setattr__(self, "is_array", True)
        if self.dimensions and self.array_size is None:
            object.__setattr__(self, "array_size", self.dimensions[0])

    def __str__(self) -> str:
        if self.is_array:
            dims = "".join(f"[{size}]" for size in self.dimensions)
            return f"{self.name}{dims}"
        return self.name

    def element_type(self) -> "JssType":
        if not self.is_array:
            raise ValueError("Tipo não é vetor.")
        if len(self.dimensions) <= 1:
            return JssType(self.name)
        return JssType(
            self.name,
            is_array=True,
            array_size=self.dimensions[1],
            dimensions=self.dimensions[1:],
        )

    def is_numeric(self) -> bool:
        return not self.is_array and self.name in {"int", "real"}

    def is_primitive(self) -> bool:
        return not self.is_array and self.name in {"int", "real", "str", "bool"}

    def is_void(self) -> bool:
        return not self.is_array and self.name == "void"

    def is_null(self) -> bool:
        return not self.is_array and self.name == "null"

INT = JssType("int")
REAL = JssType("real")
STR = JssType("str")
BOOL = JssType("bool")
VOID = JssType("void")
NULL = JssType("null")

def numeric_result(left: JssType, right: JssType) -> JssType:
    if left.name == "real" or right.name == "real":
        return REAL
    return INT

def can_assign(target: JssType, source: JssType, known_classes: set[str] | None = None) -> bool:
    known_classes = known_classes or set()

    if target == source:
        return True

    # Permite atribuir int em real.
    if target == REAL and source == INT:
        return True

    # Permite null em objeto.
    if source == NULL and target.name in known_classes and not target.is_array:
        return True

    return False

def can_cast(from_type: JssType, to_type: JssType) -> bool:
    if from_type.is_array or to_type.is_array:
        return False

    if to_type.name == "str" and from_type.name in {"int", "real", "bool", "str"}:
        return True

    if from_type.name in {"int", "real", "bool"} and to_type.name in {"int", "real", "bool"}:
        return True

    return False