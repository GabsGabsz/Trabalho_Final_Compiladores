"""Roda o pipeline completo do back-end (Jasmin -> bytecode -> JVM) para cada
arquivo de tests/backend e compara a saida exata com o valor esperado.

Equivalente universal de scripts/run_backend_tests.ps1:
    python -m src.scripts.run_backend_tests
"""

import subprocess
import sys

from . import assemble_jasmin, common, run_jasmin_class

TESTS = [
    {"file": "tests/backend/01_print_soma.jss", "expected": "Resultado: 30"},
    {"file": "tests/backend/02_fatorial.jss", "expected": "Fatorial: 120"},
    {"file": "tests/backend/03_while.jss", "expected": "Soma: 10"},
    {"file": "tests/backend/04_if_else.jss", "expected": "Maior"},
    {"file": "tests/backend/05_for_break.jss", "expected": "Soma: 6"},
    {"file": "tests/backend/06_variavel_global.jss", "expected": "Resultado: 15"},
    {"file": "tests/backend/07_bool.jss", "expected": "Liberado"},
    {"file": "tests/backend/08_casts_backend.jss", "expected": "3 10.0 true true"},
    {"file": "tests/backend/09_input_int.jss", "input": "22", "expected": "Idade: 22"},
    {"file": "tests/backend/10_input_real.jss", "input": "8.5", "expected": "Media: 8.5"},
    {"file": "tests/backend/11_input_str.jss", "input": "Joao", "expected": "Nome: Joao"},
    {"file": "tests/backend/12_vetor_int.jss", "expected": "Valor: 15"},
    {"file": "tests/backend/13_vetor_real.jss", "expected": "Nota: 8.5"},
    {"file": "tests/backend/14_vetor_str.jss", "expected": "Nome: Joao"},
    {"file": "tests/backend/15_vetor_global.jss", "expected": "Valor: 30"},
    {"file": "tests/backend/16_input_vetor.jss", "input": "10\n20", "expected": "Soma: 30"},
    {"file": "tests/backend/17_classe_ponto.jss", "expected": "Resultado: 3"},
    {"file": "tests/backend/18_classe_atributo.jss", "expected": "X: 10\nY: 20"},
    {"file": "tests/backend/19_classe_alterar_atributo.jss", "expected": "Soma: 120"},
    {"file": "tests/backend/20_classe_metodo_parametro.jss", "expected": "Resultado: 15"},
    {"file": "tests/backend/21_classe_metodo_void.jss", "expected": "Valor: 30"},
    {"file": "tests/backend/22_duas_classes.jss", "expected": "Resultado: 23"},
    {"file": "tests/backend/23_classe_real_str.jss", "expected": "Aluno: Ana\nNota: 9.5"},
    {"file": "tests/backend/24_operadores_atribuicao.jss", "expected": "X: 0"},
    {"file": "tests/backend/25_incremento_decremento.jss", "expected": "X: 11"},
    {"file": "tests/backend/26_operadores_classe_vetor.jss", "expected": "Caixa: 25\nVetor: 41"},
    {"file": "tests/backend/27_aritmetica_mista.jss", "expected": "A: 12.5\nB: 12.5\nC: 25.0\nOK: true"},
    {"file": "tests/backend/28_potencia.jss", "expected": "A: 8\nB: 25\nC: 16.5"},
    {
        "file": "tests/backend/29_programa_completo.jss",
        "expected": "Produto: Banana\nQuantidade: 6\nNumero: 11\nTotal: 142.0",
    },
    {"file": "tests/backend/30_string_concat.jss", "expected": "Valor: 10 / 2.5 / true"},
    {"file": "tests/backend/31_input_multiplos.jss", "input": "5\n2.5\nAna", "expected": "Ana 5 2.5"},
    {"file": "tests/backend/32_bool_real.jss", "expected": "false true"},
    {"file": "tests/backend/33_curto_circuito.jss", "expected": "A: 0 false\nB: 0 true"},
    {"file": "tests/backend/34_potencia_composta.jss", "expected": "X: 8"},
    {
        "file": "tests/backend/35_programa_complexo.jss",
        "expected": (
            "Logica ok\nTotal: 68 Media: 68.0\nFatorial de 5: 120\nChamadas recursivas: 5\n"
            "Potencia: 32\nZero como bool: false\nNome: Ana Idade: 30\nNova idade: 31\n"
            "Objeto nulo detectado"
        ),
    },
    {"file": "tests/backend/36_for_variantes.jss", "expected": "Soma: 6\nVoltas: 5\nParada: 4"},
    {"file": "tests/backend/37_parametros_derivados.jss", "expected": "Soma: 150\nDobro: 14"},
]


def _generate_jasmin(file: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "main.py", "--jasmin", file], capture_output=True, text=True
    )


def main(argv: list[str] | None = None) -> int:
    common.require_repo_root()
    common.print_header("TESTES DO BACK-END JASMIN")

    failed = 0

    for test in TESTS:
        file = test["file"]
        print(f"\n[BACKEND] {file}")

        compile_result = _generate_jasmin(file)
        print(compile_result.stdout.strip())

        if not compile_result.stdout.startswith("OK: codigo Jasmin gerado"):
            common.print_fail("FALHOU NA GERACAO JASMIN")
            print(compile_result.stderr.strip())
            failed += 1
            continue

        try:
            assemble_jasmin.assemble()
        except common.ScriptError as error:
            common.print_fail(f"FALHOU NA MONTAGEM JASMIN: {error}")
            failed += 1
            continue

        run_result = run_jasmin_class.run_class(stdin_text=test.get("input"), capture=True)
        run_output = run_result.stdout.strip()

        print(f"SAIDA: {run_output}")

        if run_output == test["expected"]:
            common.print_pass()
        else:
            common.print_fail()
            print(f"Esperado: {test['expected']}")
            print(f"Obtido:   {run_output}")
            failed += 1

    print()
    if failed == 0:
        common.print_pass("TODOS OS TESTES DO BACK-END PASSARAM.")
        return 0

    common.print_fail(f"{failed} TESTE(S) DO BACK-END FALHARAM.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
