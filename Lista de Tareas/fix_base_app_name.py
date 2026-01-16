from pathlib import Path
p = Path(r"Mi web\src\proyecto\base\apps.py")
text = p.read_text(encoding="utf-8-sig")
replacements = [
    ("name = 'base'", "name = 'proyecto.base'"),
    ('name = \"base\"', 'name = \"proyecto.base\"')
]
done = False
for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        done = True
if done:
    p.write_text(text, encoding="utf-8")
    print("apps.py actualizado: name -> 'proyecto.base'")
else:
    print("No se encontró 'name = \"base\"' en apps.py. No se hicieron cambios.")
