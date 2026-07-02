"""Roda a suite do front-end e depois a do back-end, parando no primeiro erro.

Equivalente universal de scripts/run_all_tests.ps1:
    python -m src.scripts.run_all_tests
"""

from . import common, run_backend_tests, run_tests


def main(argv: list[str] | None = None) -> int:
    common.print_header("EXECUTANDO TODOS OS TESTES DO JSS")

    print("\n1. TESTES DO FRONT-END")
    if run_tests.main() != 0:
        common.print_fail("FALHA NOS TESTES DO FRONT-END.")
        return 1

    print("\n2. TESTES DO BACK-END JASMIN")
    if run_backend_tests.main() != 0:
        common.print_fail("FALHA NOS TESTES DO BACK-END.")
        return 1

    print()
    common.print_pass("TODOS OS TESTES PASSARAM. FRONT-END E BACK-END FUNCIONANDO.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
