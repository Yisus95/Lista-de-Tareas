# Lista de Tareas 📝

Aplicación web desarrollada con **Django** para gestionar tareas pendientes.  
Permite a los usuarios registrarse, iniciar sesión y administrar sus tareas de forma sencilla: crear, editar, marcar como completas y eliminarlas.

---

## 🚀 Capturas de pantalla

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


## 🛠️ Tecnologías utilizadas

- **Python 3.11**
- **Django 5.x**
- **SQLite** (base de datos por defecto)
- HTML + CSS

---

## ⚙️ Instalación y uso

1.Clona el repositorio:
   ```bash
   git clone https://github.com/Yisus95/Lista-de-Tareas.git
   cd Lista-de-Tareas/src/proyecto
   ```

2.Crea un entorno virtual:
   ```bash
   python -m venv venv
   # Linux / macOS
   source venv/bin/activate
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   # Windows (cmd)
   venv\Scripts\activate
   ```

3.Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3.Si no tienes requirements.txt, instala Django y crea el archivo:
   ```bash
   pip install "Django>=5.0,<6.0"
   pip freeze > requirements.txt
   ```

4.Ejecuta migraciones:
   ```bash
   python manage.py migrate
   ```

5.Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

6.Abre en el navegador:
   ```bash
   http://127.0.0.1:8000
   ```

7.- Para salir del entorno virtual:
   ```bash
   deactivate
   ```
   ---

   **Notas rápidas**
   - Asegúrate de ejecutar los comandos desde `src/proyecto` (donde está `manage.py`).  
   - Usa `pip install -r requirements.txt` solo si `requirements.txt` existe y contiene las dependencias correctas.  
   - Si usas Windows y tienes problemas con `Activate.ps1`, abre PowerShell como administrador o usa `cmd` y el comando `venv\Scripts\activate`.

## 📋 Funcionalidades

- Registro e inicio de sesión de usuarios
- Crear nuevas tareas
- Editar tareas existentes
- Marcar tareas como completas
- Eliminar tareas
- Buscador de tareas

---

## 🔮 Mejoras futuras

- Añadir categorías o etiquetas a las tareas
- Implementar API REST con Django REST Framework
- Mejorar estilos con Bootstrap o Tailwind

---

## 👨‍💻 Autor

Proyecto creado por **Jesús (Yisus95)** como parte de su portfolio.  
Puedes ver más en [mi perfil de GitHub](https://github.com/Yisus95).


  
