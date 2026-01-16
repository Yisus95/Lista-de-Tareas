from pathlib import Path
p = Path(r"Mi web\src\proyecto\proyecto\settings.py")
text = p.read_text(encoding="utf-8-sig")

old = '"base.apps.BaseConfig"'
new = '"proyecto.base.apps.BaseConfig"'

if old in text:
    new_text = text.replace(old, new)
    p.write_text(new_text, encoding="utf-8")
    print("Reemplazado:", old, "->", new)
else:
    print("No se encontró la cadena a reemplazar. No se hicieron cambios.")
