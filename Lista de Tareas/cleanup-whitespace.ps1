Get-ChildItem -Path "Mi web/src/proyecto" -Recurse -Include *.py | ForEach-Object {
  $path = $_.FullName
  $text = Get-Content -Raw -Encoding UTF8 $path
  # Separar en líneas
  $lines = $text -split "`r?`n"
  # Quitar todas las líneas vacías al final
  while ($lines.Count -gt 0 -and ($lines[-1].Trim() -eq "")) {
    $lines = $lines[0..($lines.Count-2)]
  }
  # Reconstruir y asegurar una newline final
  $new = ($lines -join "`n") + "`n"
  Set-Content -Path $path -Value $new -Encoding UTF8
}