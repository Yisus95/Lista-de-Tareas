from pathlib import Path
names = {'pytest.ini','setup.cfg','tox.ini','pyproject.toml','.pytest.toml'}
root = Path('.').resolve()
found = []
for p in root.rglob('*'):
    if p.name in names:
        found.append(p)
if not found:
    print("No se encontraron archivos de configuración candidatos (pytest.ini, setup.cfg, tox.ini, pyproject.toml, .pytest.toml).")
else:
    print("Archivos encontrados:")
    for f in found:
        print(" -", f)
    print()
    for f in found:
        try:
            _ = f.read_text(encoding='utf-8')
            print("OK   :", f)
        except Exception as e:
            print("ERROR:", f, "->", type(e).__name__, e)
