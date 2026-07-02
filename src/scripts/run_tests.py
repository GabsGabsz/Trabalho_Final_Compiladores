"""Roda a suite de testes do front-end (tests/success e tests/errors).

Equivalente universal de scripts/run_tests.ps1:
    python -m src.scripts.run_tests
"""

import subprocess
import sys
from pathlib import Path

from . import common


def _run_compiler(file: Path) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "main.py", str(file)], capture_output=True, text=True)


def _check(files: list[Path], expected_prefix: str, label: str) -> int:
    failed = 0
    for file in sorted(files, key=lambda f: f.name):
        print(f"\n[{label}] {file.name}")
        result = _run_compiler(file)
        print(result.stdout.strip())

        if not result.stdout.startswith(expected_prefix):
            common.print_fail(f"FALHOU: era esperado '{expected_prefix}'.")
            failed += 1
        else:
            common.print_pass()

    return failed


def main(argv: list[str] | None = None) -> int:
    common.require_repo_root()

    common.print_header("TESTES DE SUCESSO")
    failed = _check(list((common.TESTS_DIR / "success").glob("*.jss")), "OK:", "SUCESSO")

    print()
    common.print_header("TESTES DE ERRO")
    failed += _check(list((common.TESTS_DIR / "errors").glob("*.jss")), "ERRO", "ERRO ESPERADO")

    print()
    if failed == 0:
        common.print_pass("TODOS OS TESTES DO FRONT-END PASSARAM.")
        return 0

    common.print_fail(f"{failed} TESTE(S) DO FRONT-END FALHARAM.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
