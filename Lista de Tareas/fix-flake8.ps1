# fix-flake8.ps1
# Backup y arreglos automáticos (trailing blanks, eliminar imports concretos, espaciado en urls), luego run tools.

$project = "Mi web/src/proyecto"

# Lista de ficheros a tocar (según flake8)
$files = @(
  "$project/base/__init__.py",
  "$project/base/admin.py",
  "$project/base/apps.py",
  "$project/base/models.py",
  "$project/base/tests.py",
  "$project/base/urls.py",
  "$project/base/views.py",
  "$project/manage.py",
  "$project/proyecto/__init__.py",
  "$project/proyecto/asgi.py",
  "$project/proyecto/settings.py",
  "$project/proyecto/urls.py",
  "$project/proyecto/wsgi.py"
)

Write-Host "=== BACKUP & FIX TRAILING BLANKS ==="
foreach ($p in $files) {
  if (Test-Path $p) {
    Copy-Item $p ($p + ".bak") -Force
    try {
      $txt = Get-Content -Raw -Encoding UTF8 $p
      # Normaliza finales: elimina líneas vacías al final y deja exactamente CRLF final
      $new = $txt -replace "(\r?\n)+\z", "`r`n"
      if ($new -ne $txt) {
        Set-Content -Path $p -Value $new -Encoding UTF8
        Write-Host "Fixed trailing blanks: $p"
      } else {
        Write-Host "No change: $p"
      }
    } catch {
      Write-Host "Error reading $p : $_"
    }
  } else {
    Write-Host "Not found: $p"
  }
}

# Eliminar imports específicos reportados por flake8 (si existen)
Write-Host "=== REMOVE SPECIFIC UNUSED IMPORT LINES (if present) ==="
# tests.py: remove 'from django.test import TestCase'
$testsPath = "$project/base/tests.py"
if (Test-Path $testsPath) {
  $content = Get-Content -Raw $testsPath -Encoding UTF8
  $new = $content -replace "(?m)^\s*from\s+django\.test\s+import\s+TestCase\s*\r?\n", ""
  if ($new -ne $content) {
    Set-Content -Path $testsPath -Value $new -Encoding UTF8
    Write-Host "Removed TestCase import if present in tests.py"
  } else {
    Write-Host "No TestCase import found/removed in tests.py"
  }
}

# views.py: remove LogoutView and render imports if present
$viewsPath = "$project/base/views.py"
if (Test-Path $viewsPath) {
  $content = Get-Content -Raw $viewsPath -Encoding UTF8
  $new = $content -replace "(?m)^\s*from\s+django\.contrib\.auth\.views\s+import\s+LogoutView\s*\r?\n", ""
  $new = $new -replace "(?m)^\s*from\s+django\.shortcuts\s+import\s+render\s*\r?\n", $new
  # (second replace above purposely uses $new on RHS to continue removing both)
  if ($new -ne $content) {
    Set-Content -Path $viewsPath -Value $new -Encoding UTF8
    Write-Host "Removed LogoutView/render imports if present in views.py"
  } else {
    Write-Host "No LogoutView/render imports found/removed in views.py"
  }
}

# Arreglar comas sin espacio en base/urls.py (backup ya creado)
$urlsPath = "$project/base/urls.py"
if (Test-Path $urlsPath) {
  $content = Get-Content -Raw $urlsPath -Encoding UTF8
  $fixed = $content -replace ',(?=\S)', ', '
  if ($fixed -ne $content) {
    Set-Content -Path $urlsPath -Value $fixed -Encoding UTF8
    Write-Host "Applied comma spacing fix to base/urls.py"
  } else {
    Write-Host "No comma spacing changes needed in base/urls.py"
  }
}

# Instalar herramientas si no están (intenta pip; ignora errores si ya instaladas)
Write-Host "=== INSTALL/ENSURE TOOLS (autoflake isort black) ==="
pip install autoflake isort black --quiet

# Ejecutar autoflake sólo en el proyecto (intento seguro)
Write-Host "=== RUN AUTOFLAKE ==="
autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive $project 2>&1 | Write-Host

# isort + black
Write-Host "=== RUN ISORT ==="
isort $project 2>&1 | Write-Host
Write-Host "=== RUN BLACK ==="
black $project 2>&1 | Write-Host

# Ejecutar flake8 y guardar salida
Write-Host "=== RUN FLAKE8 AND WRITE flake8-after-auto.txt ==="
flake8 $project | Tee-Object -FilePath flake8-after-auto.txt
Write-Host "=== DONE. See flake8-after-auto.txt ==="