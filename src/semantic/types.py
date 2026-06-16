from dataclasses import dataclass


@dataclass(frozen=True)
class JssType:
    name: str
    is_array: bool = False
    array_size: int | None = None

    def __str__(self) -> str:
        if self.is_array:
            return f"{self.name}[{self.array_size}]"
        return self.name

    def element_type(self) -> "JssType":
        if not self.is_array:
            raise ValueError("Tipo não é vetor.")
        return JssType(self.name)

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