from pathlib import Path

p = Path('pytest.ini')
if not p.exists():
    print("ERROR: pytest.ini no existe en la carpeta actual:", Path('.').resolve())
else:
    # Leer con 'utf-8-sig' -> si hay BOM, se elimina al leer
    text = p.read_text(encoding='utf-8-sig')

    # Contenido recomendado (ajusta si necesitas otras opciones)
    desired = """[pytest]
# Django settings
DJANGO_SETTINGS_MODULE = proyecto.settings

# Qué archivos/patrones contienen tests en tu proyecto
python_files = tests.py test_*.py *_tests.py

# Evitar que pytest recorra directorios no relevantes (incluye .venv)
norecursedirs = .git .venv venv env build dist .tox node_modules
"""

    # Si el contenido real es distinto al recomendado lo reescribimos; 
    # si es igual, lo reescribimos igualmente para asegurarnos de no tener BOM.
    if text.strip() != desired.strip():
        p.write_text(desired, encoding='utf-8')
        print("pytest.ini reescrito con el contenido recomendado y guardado en UTF-8 sin BOM.")
    else:
        p.write_text(text, encoding='utf-8')
        print("pytest.ini guardado en UTF-8 sin BOM (contenido sin cambios).")
