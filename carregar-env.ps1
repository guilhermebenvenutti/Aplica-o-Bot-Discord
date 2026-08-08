Get-Content .\.env | ForEach-Object {
    if ($_ -match '^\s*([^#=]+?)\s*=\s*(.*)$') {
        Set-Item -Path ("env:" + $Matches[1]) -Value $Matches[2]
    }
}

Write-Host "Carregado: CANAL=$env:DISCORD_CANAL_ID"