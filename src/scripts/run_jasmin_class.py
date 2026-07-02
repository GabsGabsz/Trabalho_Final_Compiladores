"""Executa uma classe ja montada em output/classes na JVM.

Equivalente universal de scripts/run_jasmin_class.ps1:
    python -m src.scripts.run_jasmin_class [NomeDaClasse]
"""

import sys
from pathlib import Path

from . import common


def run_class(
    class_name: str = "Main",
    classes_dir: Path = common.OUTPUT_CLASSES_DIR,
    stdin_text: str | None = None,
    capture: bool = False,
):
    common.require_repo_root()
    return common.run_java_class(classes_dir, class_name, stdin_text=stdin_text, capture=capture)


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    class_name = argv[0] if argv else "Main"

    try:
        result = run_class(class_name)
    except common.ScriptError as error:
        print(f"ERRO: {error}")
        return 1

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
