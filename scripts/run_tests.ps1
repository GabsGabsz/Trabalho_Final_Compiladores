$failed = 0

Write-Host "=============================="
Write-Host "TESTES DE SUCESSO"
Write-Host "=============================="

Get-ChildItem tests\success\*.jss | Sort-Object Name | ForEach-Object {
    Write-Host "`n[SUCESSO] $($_.Name)"

    $output = python main.py $_.FullName
    Write-Host $output

    if (-not ($output -like "OK:*")) {
        Write-Host "FALHOU: era esperado OK." -ForegroundColor Red
        $script:failed++
    } else {
        Write-Host "PASSOU" -ForegroundColor Green
    }
}

Write-Host "`n=============================="
Write-Host "TESTES DE ERRO"
Write-Host "=============================="

Get-ChildItem tests\errors\*.jss | Sort-Object Name | ForEach-Object {
    Write-Host "`n[ERRO ESPERADO] $($_.Name)"

    $output = python main.py $_.FullName
    Write-Host $output

    if (-not ($output -like "ERRO*")) {
        Write-Host "FALHOU: era esperado ERRO." -ForegroundColor Red
        $script:failed++
    } else {
        Write-Host "PASSOU" -ForegroundColor Green
    }
}

Write-Host "`n=============================="

if ($failed -eq 0) {
    Write-Host "TODOS OS TESTES DO FRONT-END PASSARAM." -ForegroundColor Green
    exit 0
} else {
    Write-Host "$failed TESTE(S) DO FRONT-END FALHARAM." -ForegroundColor Red
    exit 1
}