if (!(Test-Path "output\classes")) {
    New-Item -ItemType Directory -Path "output\classes" | Out-Null
}

Remove-Item output\classes\*.class -ErrorAction SilentlyContinue

$files = Get-ChildItem output\*.j

if ($files.Count -eq 0) {
    Write-Host "Nenhum arquivo .j encontrado em output." -ForegroundColor Red
    exit 1
}

java -jar tools\jasmin.jar -d output\classes $files.FullName