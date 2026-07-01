$ErrorActionPreference = "Stop"

$tests = @(
    @{ File = "tests\prof\1_basics.jss"; Expected = $null; Input = $null },
    @{ File = "tests\prof\2_operators.jss"; Expected = $null; Input = $null },
    @{ File = "tests\prof\3_control_flow.jss"; Expected = $null; Input = $null },
    @{ File = "tests\prof\4_strings_casts.jss"; Expected = $null; Input = "1 2 3`nAna Bia`n" },
    @{ File = "tests\prof\5_classes.jss"; Expected = $null; Input = $null },
    @{ File = "tests\prof\6_functions.jss"; Expected = $null; Input = $null }
)

$failed = 0

Write-Host "=============================="
Write-Host "TESTES DO PROFESSOR - FRONT-END"
Write-Host "=============================="

foreach ($test in $tests) {
    Write-Host "`n[FRONT] $($test.File)"
    $output = python main.py $test.File
    Write-Host $output

    if (-not ($output -like "OK:*")) {
        Write-Host "FALHOU NO FRONT-END" -ForegroundColor Red
        $failed++
    } else {
        Write-Host "PASSOU" -ForegroundColor Green
    }
}

Write-Host "`n=============================="
Write-Host "TESTES DO PROFESSOR - BACK-END"
Write-Host "=============================="

foreach ($test in $tests) {
    Write-Host "`n[BACK] $($test.File)"
    $compileOutput = python main.py --jasmin $test.File
    Write-Host $compileOutput

    if (-not ($compileOutput -like "OK: codigo Jasmin gerado*")) {
        Write-Host "FALHOU NA GERACAO JASMIN" -ForegroundColor Red
        $failed++
        continue
    }

    .\scripts\assemble_jasmin.ps1 | Out-Null

    if ($test.Input -ne $null) {
        $runOutput = ($test.Input | java -cp output\classes Main) -join "`n"
    } else {
        $runOutput = (java -cp output\classes Main) -join "`n"
    }

    Write-Host $runOutput
    Write-Host "PASSOU" -ForegroundColor Green
}

Write-Host "`n=============================="

if ($failed -eq 0) {
    Write-Host "TODOS OS TESTES DO PROFESSOR PASSARAM." -ForegroundColor Green
    exit 0
} else {
    Write-Host "$failed TESTE(S) FALHARAM." -ForegroundColor Red
    exit 1
}
