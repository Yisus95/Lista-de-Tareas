# Lista-de-Tareas

Aplicación de lista de tareas desarrollada con Django (backend) y Python, enfocada en practicar buenas prácticas de arquitectura, seguridad básica y automatización con CI en GitHub Actions.

**Stack principal:**
- Python 3 · Django
- HTML, CSS, JavaScript
- Pytest
- GitHub Actions (CI)

[![CI](https://github.com/Yisus95/Lista-de-Tareas/actions/workflows/ci.yml/badge.svg)](https://github.com/Yisus95/Lista-de-Tareas/actions/workflows/ci.yml) 
![pytest](https://img.shields.io/badge/tests-pytest-brightgreen) 
![style: black](https://img.shields.io/badge/format-black-000000)
![Django](https://img.shields.io/badge/django-backend-green)
![License: MIT](https://img.shields.io/badge/license-MIT-yellow)

Estado
- CI: ✅ (workflow `ci-minimal.yml` ejecuta tests)
- Presentable: ✅ (limpieza básica y .gitignore aplicado)

## Capturas

<p align="center">
<img src="docs/screenshots/Acceso.png" alt="Acceso" width="800"><br>
<em>Acceso o registro de nuevo usuario.</em>
</p>

<p align="center">
<img src="docs/screenshots/Regristro.png" alt="Registro" width="800"><br>
<em>Registro de nuevos usuarios.</em>
</p>

<p align="center">
<img src="docs/screenshots/Lista-Tareas.png" alt="Lista de Tareas" width="800"><br>
<em>Lista con buscador, creación rápida y estados de tarea.</em>
</p>

<p align="center">
<img src="docs/screenshots/Crear-Tarea.png" alt="Crear nueva tarea" width="800"><br>
<em>Crear nueva tarea.</em>
</p>

<p align="center">
<img src="docs/screenshots/Confirm-Borrar.png" alt="Borrar tarea" width="800"><br>
<em>Confirmación y mensaje flash al borrar tarea.</em>
</p>

## Tecnologías y buenas prácticas

- **Backend:** Django (vistas, modelos, autenticación de usuarios)
- **Base de datos:** SQLite (configurable)
- **Frontend:** HTML + CSS + JavaScript clásico
- **Autenticación:** registro, login y protección de vistas por usuario
- **Testing:** Pytest (tests ejecutados en CI)
- **CI:** GitHub Actions (`ci-minimal.yml`) ejecutando tests en cada push/PR
- **Calidad de código:** uso de `.gitignore`, estructura de proyecto limpia, separación de responsabilidades

  ## Qué demuestro con este proyecto

- Capacidad para crear una aplicación web completa con Django (registro, login y CRUD por usuario).
- Uso de Git de forma ordenada: ramas, commits claros y limpieza del historial.
- Configuración de Integración Continua (CI) con GitHub Actions para asegurar que los tests se ejecutan en cada cambio.
- Gestión correcta de entornos y secretos: `.gitignore` para excluir `.env`, `venv`, bases de datos locales, etc.
- Documentación: instrucciones claras para clonar, instalar dependencias y ejecutar la aplicación y los tests.

## Instalación (local)
1. Clonar
```bash
git clone https://github.com/Yisus95/Lista-de-Tareas.git
cd Lista-de-Tareas
```

2. Crear entorno virtual e instalar dependencias
```bash
python -m venv .venv
.\.venv\Scripts\Activate    # Windows
# source .venv/bin/activate # macOS / Linux
pip install -r requirements.txt
```

3. Migraciones (si aplican, p. ej. Django)
```bash
python manage.py migrate
python manage.py runserver
```

Accede a: http://127.0.0.1:8000

## Tests
Ejecutar tests locales:
```bash
pytest -q
```

## CI
GitHub Actions ejecuta `ci-minimal.yml` en cada push/PR y corre los tests. El workflow está en `.github/workflows/ci-minimal.yml`.

## Estructura del repo
- `src/proyecto/` — código fuente principal  
- `docs/screenshots/` — capturas usadas en este README  
- `.github/workflows/ci-minimal.yml` — workflow CI  
- `.gitignore` — archivos ignorados (venv, tmpenv, node_modules, db)

## Qué he limpiado / recomendaciones
- Ignorar y eliminar del índice carpetas de entornos y DB locales (añadir `.gitignore` si falta).  
- Mantener `main` estable; usar ramas por funcionalidad y PRs con `Squash and merge` para un historial limpio.  
- Si hay archivos grandes en el historial y quieres reducir el tamaño del repo, usar BFG/git-filter-repo (te puedo ayudar si lo deseas).

## Para reclutadores

Este proyecto forma parte de mi portfolio y está pensado para mostrar:

- Desarrollo backend con Django.
- Buenas prácticas de Git y GitHub.
- Automatización con CI.
- Capacidad para documentar y mantener un proyecto.

Si quieres ver más proyectos o hablar conmigo, puedes contactarme por GitHub o por [tu email / LinkedIn si quieres ponerlo].

## Licencia
- MIT (añade un `LICENSE` si quieres publicar con licencia).

## Contacto
- Autor: Yisus95 — https://github.com/Yisus95
```
