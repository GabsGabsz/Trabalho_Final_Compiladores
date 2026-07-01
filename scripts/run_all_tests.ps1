$ErrorActionPreference = "Stop"

Write-Host "===================================="
Write-Host "EXECUTANDO TODOS OS TESTES DO JSS"
Write-Host "===================================="

Write-Host "`n===================================="
Write-Host "1. TESTES DO FRONT-END"
Write-Host "===================================="

.\scripts\run_tests.ps1

if ($LASTEXITCODE -ne 0) {
    Write-Host "`nFALHA NOS TESTES DO FRONT-END." -ForegroundColor Red
    exit 1
}

Write-Host "`n===================================="
Write-Host "2. TESTES DO BACK-END JASMIN"
Write-Host "===================================="

.\scripts\run_backend_tests.ps1

if ($LASTEXITCODE -ne 0) {
    Write-Host "`nFALHA NOS TESTES DO BACK-END." -ForegroundColor Red
    exit 1
}

Write-Host "`n===================================="
Write-Host "TODOS OS TESTES PASSARAM."
Write-Host "FRONT-END E BACK-END FUNCIONANDO."
Write-Host "====================================" -ForegroundColor Green