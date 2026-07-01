from pathlib import Path


class CodeWriter:
    def __init__(self):
        self.lines: list[str] = []
        self.indent_level = 0

    def emit(self, line: str = ""):
        if line:
            self.lines.append("    " * self.indent_level + line)
        else:
            self.lines.append("")

    def emit_label(self, label: str):
        self.lines.append(f"{label}:")

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1

    def text(self) -> str:
        return "\n".join(self.lines) + "\n"

    def save(self, path: str | Path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        # Sem BOM. Jasmin nao gosta de arquivo com caractere invisivel no inicio.
        path.write_text(self.text(), encoding="ascii")