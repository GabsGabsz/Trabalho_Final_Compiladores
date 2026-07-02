"""Roda os arquivos fornecidos pelo professor (tests/prof), front-end e
back-end, sem asserção estrita de saída (só confere OK/ERRO conforme
esperado para cada arquivo).

Equivalente universal de scripts/run_professor_tests.ps1:
    python -m src.scripts.run_professor_tests
"""

import subprocess
import sys

from . import assemble_jasmin, common, run_jasmin_class

POSITIVE_TESTS = [
    {"file": "tests/prof/1_basics.jss"},
    {"file": "tests/prof/2_operators.jss"},
    {"file": "tests/prof/3_control_flow.jss"},
    {"file": "tests/prof/4_strings_casts.jss", "input": "1 2 3\nAna Bia\n"},
    {"file": "tests/prof/5_classes.jss"},
]

# 6_functions.jss declara "function int[5] criarSequencia(...)", ou seja, uma
# funcao que retorna vetor. A especificacao (secao 4.4) proibe isso e o
# professor confirmou que este arquivo e um teste negativo, entao o compilador
# deve rejeita-lo por regra semantica. Tratado como erro esperado, junto com
# 7_errors.jss e 8_erros_funcao.jss (comentados no proprio arquivo como
# "arquivo deve falhar na compilacao").
ERROR_TESTS = [
    "tests/prof/6_functions.jss",
    "tests/prof/7_errors.jss",
    "tests/prof/8_erros_funcao.jss",
]


def _run_compiler(file: str, *, jasmin: bool = False) -> subprocess.CompletedProcess:
    args = [sys.executable, "main.py"]
    if jasmin:
        args.append("--jasmin")
    args.append(file)
    return subprocess.run(args, capture_output=True, text=True)


def main(argv: list[str] | None = None) -> int:
    common.require_repo_root()
    failed = 0

    common.print_header("TESTES DO PROFESSOR - FRONT-END")
    for test in POSITIVE_TESTS:
        print(f"\n[FRONT] {test['file']}")
        result = _run_compiler(test["file"])
        print(result.stdout.strip())

        if not result.stdout.startswith("OK:"):
            common.print_fail("FALHOU NO FRONT-END")
            failed += 1
        else:
            common.print_pass()

    print()
    common.print_header("TESTES DO PROFESSOR - BACK-END")
    for test in POSITIVE_TESTS:
        print(f"\n[BACK] {test['file']}")
        compile_result = _run_compiler(test["file"], jasmin=True)
        print(compile_result.stdout.strip())

        if not compile_result.stdout.startswith("OK: codigo Jasmin gerado"):
            common.print_fail("FALHOU NA GERACAO JASMIN")
            failed += 1
            continue

        try:
            assemble_jasmin.assemble()
        except common.ScriptError as error:
            common.print_fail(f"FALHOU NA MONTAGEM JASMIN: {error}")
            failed += 1
            continue

        run_result = run_jasmin_class.run_class(stdin_text=test.get("input"), capture=True)
        print(run_result.stdout.strip())
        common.print_pass()

    print()
    common.print_header("TESTES DO PROFESSOR - CASOS DE ERRO")
    for file in ERROR_TESTS:
        print(f"\n[ERRO ESPERADO] {file}")
        result = _run_compiler(file)
        print(result.stdout.strip())

        if not result.stdout.startswith("ERRO"):
            common.print_fail("FALHOU: era esperado ERRO.")
            failed += 1
        else:
            common.print_pass()

    print()
    if failed == 0:
        common.print_pass("TODOS OS TESTES DO PROFESSOR PASSARAM.")
        return 0

    common.print_fail(f"{failed} TESTE(S) FALHARAM.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
