"""Ponto de entrada unico para os scripts de automacao.

    python -m src.scripts <comando> [args...]

Cada comando tambem pode ser chamado diretamente pelo seu proprio modulo,
por exemplo 'python -m src.scripts.run_tests'.
"""

import sys

from . import (
    assemble_jasmin,
    generate_parser,
    run_all_tests,
    run_backend_tests,
    run_jasmin_class,
    run_professor_tests,
    run_tests,
)

COMMANDS = {
    "generate_parser": generate_parser.main,
    "assemble_jasmin": assemble_jasmin.main,
    "run_jasmin_class": run_jasmin_class.main,
    "run_tests": run_tests.main,
    "run_backend_tests": run_backend_tests.main,
    "run_professor_tests": run_professor_tests.main,
    "run_all_tests": run_all_tests.main,
}


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    if not argv or argv[0] not in COMMANDS:
        print("uso: python -m src.scripts <comando> [args...]")
        print(f"comandos disponiveis: {', '.join(sorted(COMMANDS))}")
        return 1

    command, rest = argv[0], argv[1:]
    return COMMANDS[command](rest)


if __name__ == "__main__":
    raise SystemExit(main())
