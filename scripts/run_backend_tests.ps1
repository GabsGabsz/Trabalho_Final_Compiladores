$ErrorActionPreference = "Stop"

$tests = @(
    @{ File = "tests\backend\01_print_soma.jss"; Expected = "Resultado: 30" },
    @{ File = "tests\backend\02_fatorial.jss"; Expected = "Fatorial: 120" },
    @{ File = "tests\backend\03_while.jss"; Expected = "Soma: 10" },
    @{ File = "tests\backend\04_if_else.jss"; Expected = "Maior" },
    @{ File = "tests\backend\05_for_break.jss"; Expected = "Soma: 6" },
    @{ File = "tests\backend\06_variavel_global.jss"; Expected = "Resultado: 15" },
    @{ File = "tests\backend\07_bool.jss"; Expected = "Liberado" },
    @{ File = "tests\backend\08_casts_backend.jss"; Expected = "3 10.0 true true" },

    @{ File = "tests\backend\09_input_int.jss"; Input = "22"; Expected = "Idade: 22" },
    @{ File = "tests\backend\10_input_real.jss"; Input = "8.5"; Expected = "Media: 8.5" },
    @{ File = "tests\backend\11_input_str.jss"; Input = "Joao"; Expected = "Nome: Joao" },

    @{ File = "tests\backend\12_vetor_int.jss"; Expected = "Valor: 15" },
    @{ File = "tests\backend\13_vetor_real.jss"; Expected = "Nota: 8.5" },
    @{ File = "tests\backend\14_vetor_str.jss"; Expected = "Nome: Joao" },
    @{ File = "tests\backend\15_vetor_global.jss"; Expected = "Valor: 30" },
    @{ File = "tests\backend\16_input_vetor.jss"; Input = "10`n20"; Expected = "Soma: 30" },

    @{ File = "tests\backend\17_classe_ponto.jss"; Expected = "Resultado: 3" },
    @{ File = "tests\backend\18_classe_atributo.jss"; Expected = "X: 10`nY: 20" },
    @{ File = "tests\backend\19_classe_alterar_atributo.jss"; Expected = "Soma: 120" },
    @{ File = "tests\backend\20_classe_metodo_parametro.jss"; Expected = "Resultado: 15" },
    @{ File = "tests\backend\21_classe_metodo_void.jss"; Expected = "Valor: 30" },
    @{ File = "tests\backend\22_duas_classes.jss"; Expected = "Resultado: 23" },
    @{ File = "tests\backend\23_classe_real_str.jss"; Expected = "Aluno: Ana`nNota: 9.5" },

    @{ File = "tests\backend\24_operadores_atribuicao.jss"; Expected = "X: 0" },
    @{ File = "tests\backend\25_incremento_decremento.jss"; Expected = "X: 11" },
    @{ File = "tests\backend\26_operadores_classe_vetor.jss"; Expected = "Caixa: 25`nVetor: 41" },
    @{ File = "tests\backend\27_aritmetica_mista.jss"; Expected = "A: 12.5`nB: 12.5`nC: 25.0`nOK: true" },
    @{ File = "tests\backend\28_potencia.jss"; Expected = "A: 8`nB: 25`nC: 16.5" },
    @{ File = "tests\backend\29_programa_completo.jss"; Expected = "Produto: Banana`nQuantidade: 6`nNumero: 11`nTotal: 142.0" },

    @{ File = "tests\backend\30_string_concat.jss"; Expected = "Valor: 10 / 2.5 / true" },
    @{ File = "tests\backend\31_input_multiplos.jss"; Input = "5`n2.5`nAna"; Expected = "Ana 5 2.5" },
    @{ File = "tests\backend\32_bool_real.jss"; Expected = "false true" },
    @{ File = "tests\backend\33_curto_circuito.jss"; Expected = "A: 0 false`nB: 0 true" },
    @{ File = "tests\backend\34_potencia_composta.jss"; Expected = "X: 8" },
    @{ File = "tests\backend\35_programa_complexo.jss"; Expected = "Logica ok`nTotal: 68 Media: 68.0`nFatorial de 5: 120`nChamadas recursivas: 5`nPotencia: 32`nZero como bool: false`nNome: Ana Idade: 30`nNova idade: 31`nObjeto nulo detectado" }
)

$failed = 0

Write-Host "=============================="
Write-Host "TESTES DO BACK-END JASMIN"
Write-Host "=============================="

foreach ($test in $tests) {
    Write-Host "`n[BACKEND] $($test.File)"

    $compileOutput = Get-Content -Raw $test.File | python main.py --jasmin
    Write-Host $compileOutput

    if (-not ($compileOutput -like "OK: codigo Jasmin gerado*")) {
        Write-Host "FALHOU NA GERACAO JASMIN" -ForegroundColor Red
        $failed++
        continue
    }

    $assembleOutput = .\scripts\assemble_jasmin.ps1
    Write-Host $assembleOutput

    if ($test.ContainsKey("Input")) {
        $runOutput = ($test.Input | java -cp output\classes Main) -join "`n"
    } else {
        $runOutput = (.\scripts\run_jasmin_class.ps1) -join "`n"
    }

    Write-Host "SAIDA: $runOutput"

    if ($runOutput.Trim() -eq $test.Expected) {
        Write-Host "PASSOU" -ForegroundColor Green
    } else {
        Write-Host "FALHOU" -ForegroundColor Red
        Write-Host "Esperado: $($test.Expected)"
        Write-Host "Obtido:   $runOutput"
        $failed++
    }
}

Write-Host "`n=============================="

if ($failed -eq 0) {
    Write-Host "TODOS OS TESTES DO BACK-END PASSARAM." -ForegroundColor Green
    exit 0
} else {
    Write-Host "$failed TESTE(S) DO BACK-END FALHARAM." -ForegroundColor Red
    exit 1
}
