CRUD Sencillo en Django
Este es un CRUD básico desarrollado en Django, utilizando PostgreSQL, Bootstrap, DataTables y SweetAlert2. 
Este proyecto es parte de mi aprendizaje en Django y lo iré mejorando con el tiempo.

Tecnologías utilizadas
Python (Django)

PostgreSQL

Bootstrap (para estilos)

DataTables (para mejorar las tablas)

SweetAlert2 (para alertas interactivas)

Estructura del Proyecto

Crud_Sencillo/
│── mi_app/                 # Aplicación principal
│   ├── migrations/         # Migraciones de la base de datos
│   ├── templates/          # Plantillas HTML
│   ├── __init__.py         # Indica que es un módulo de Python
│   ├── admin.py            # Configuración del panel de administración
│   ├── apps.py             # Configuración de la aplicación
│   ├── forms.py            # Formularios de Django
│   ├── models.py           # Modelos de base de datos
│   ├── tests.py            # Pruebas unitarias
│   ├── urls.py             # Rutas de la aplicación
│   ├── views.py            # Lógica de las vistas
│
│── Crud_Sencillo/          # Configuración global del proyecto
│   ├── __init__.py         
│   ├── asgi.py             # Configuración ASGI
│   ├── settings.py         # Configuración del proyecto Django
│   ├── urls.py             # Rutas principales del proyecto
│   ├── wsgi.py             # Configuración WSGI
│
│── venv/                   # Entorno virtual (no se sube a GitHub)
│── manage.py               # Script principal de Django
│── requirements.txt        # Dependencias del proyecto
│── .gitignore              # Archivos ignorados por Git

Captura de Pantalla
![image](https://github.com/user-attachments/assets/a562ced0-06db-4361-9993-eaaa756478f7)


Instalación y configuración
1. Clonar el repositorio

git clone https://github.com/crisschn007/Crud_Sencillo_Django.git
cd Crud_Sencillo_Django

2. Crear y activar un entorno virtual

python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate  # En Windows

3. Instalar dependencias
pip install -r requirements.txt

5. Configurar la base de datos en settings.py y Crear la Base de datos en PostgresSQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Crud_Sencillo',  # Cambia esto por el nombre de tu BD
        'USER': 'postgres',         # Usuario de PostgreSQL
        'PASSWORD': '',  # Ingresar la contraseña de PostgreSQL
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



6. Aplicar migraciones y ejecutar el servidor

python manage.py migrate
python manage.py runserver

Próximos pasos
  1. Seguir mejorando mis habilidades en Django.
  2. Agregar autenticación de usuarios.
  3. Implementar más funciones avanzadas.

Autor
Cristian Rodolfo Chún Ramos
