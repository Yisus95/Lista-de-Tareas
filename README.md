# Lista de Tareas

![CI](https://github.com/Yisus95/Lista-de-Tareas/actions/workflows/test.yml/badge.svg) ![pytest](https://img.shields.io/badge/tests-pytest-brightgreen) ![style: black](https://img.shields.io/badge/format-black-000000)

Pequeña aplicación Django para gestionar tareas (crear, editar, listar, marcar completadas y eliminar). Incluye notificaciones tipo "flash" para feedback al usuario — ahora también muestra un flash al eliminar una tarea. Este repositorio incluye tests (pytest), formateo (black) y linters (flake8/isort).

## Capturas

<p align="center">
<img src="https://github.com/user-attachments/assets/65b8c684-2d31-424b-8790-4acf11c42f2e" alt="Acceso" width="800"><br>
<em>Acceso o Registro de nuevo usuario.</em>
</p>

<p align="center">
<img src="https://github.com/user-attachments/assets/edde42f8-be92-42c0-9bbc-c09e87354b49" alt="Registro" width="800"><br>
<em>Registro de nuevos usuarios.</em>
</p>

<p align="center">
<img src="https://github.com/user-attachments/assets/f992a670-c502-4df1-89eb-4eb119baffdf" alt="Lista de Tareas" width="800"><br>
<em>Lista con buscador, creación rápida y estados de tarea.</em>
</p>

<p align="center">
<img src="https://github.com/user-attachments/assets/4c2bd23a-a1be-45a9-b918-51ea63bc3595" alt="Crear nueva tarea" width="800"><br>
<em>Crear nueva tarea.</em>
</p>

<p align="center">
<img src="https://github.com/user-attachments/assets/33610cd3-4b61-413a-9b3f-84b6a1b91cc7" alt="Borrar tarea" width="800"><br>
<em>Borrar tarea.</em>
</p>


## Características
- CRUD de tareas (crear, listar, editar, borrar).
- Búsqueda por título.
- Marcar como completada.
- Confirmación de eliminación y mensaje flash al borrar.
- Mensajes flash estilizados y auto-ocultado (CSS + JS).
- Protección: las vistas CRUD filtran por usuario (no puedes tocar tareas ajenas).

## Quick start (local, lo mínimo)
```bash
git clone https://github.com/Yisus95/Lista-de-Tareas.git
cd Lista-de-Tareas/src/proyecto

python -m venv .venv
# PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt

# migraciones
python manage.py migrate

# arrancar servidor
python manage.py runserver
```
Visitar: http://localhost:8000

## Cómo probar el flash al borrar (rápido)
1. Inicia sesión con un usuario.
2. Crea una tarea (si no hay).
3. Ve a la lista, elimina una tarea y confirma.
4. Deberías ver: `¡Tarea «<titulo>» eliminada correctamente!` en la parte superior.

## Tests / Lint / Format
- Tests: pytest
- Formateo: black
- Lint: flake8, isort

Ejecutar localmente:
```bash
# tests
pytest -q

# format check
black --check .

# lint
flake8
isort --check-only .
```

## Uso rápido con Makefile (opcional)
Si has añadido el `Makefile`, puedes usar:
```bash
# instalar deps y migrar
make setup

# correr servidor
make run

# ejecutar tests
make test

# lint y format checks
make lint
```

## CI
Hay un workflow de GitHub Actions (`.github/workflows/test.yml`) que:
- instala dependencias,
- ejecuta black/isort/flake8,
- ejecuta pytest.

El badge arriba mostrará el estado del workflow.

## Buenas prácticas / Notas
- No subir `.env`, `.venv` ni backups. Añádelos a `.gitignore`.
- Quitar `print()` de depuración; usar logging.
- Crear ramas por feature y abrir Pull Requests.
- Añadir capturas y badges para hacer el proyecto más presentable como portfolio.

## Contribuir / Contacto
Abrir issues o PRs. Autor: `Yisus95` (GitHub).

## Licencia
MIT (u otra que prefieras).
