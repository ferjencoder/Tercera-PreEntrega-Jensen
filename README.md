# Sistema de Gestión de Proyectos

## Descripción

Este proyecto es un sistema de gestión de proyectos desarrollado con Django. Permite gestionar proyectos, tareas, equipos y miembros de los equipos, proporcionando una herramienta completa para la planificación y seguimiento de proyectos.

## Requisitos

- Python 3.x
- Django

## Instalación

1. Clona este repositorio: 
```bash
git clone <URL del repositorio>
```
2. Navega al directorio del proyecto: 
```bash
cd <nombre_del_proyecto>
```
3. Instala las dependencias: 
```bash
pip install -r requirements.txt
```
4. Realiza las migraciones: 
```bash
python manage.py migrate
```
5. Ejecuta el servidor de desarrollo: 
```bash
python manage.py runserver
```

## Uso

1. Navega a `http://127.0.0.1:8000/` en tu navegador.
2. Utiliza la navegación para acceder a las secciones de Proyectos, Tareas, Equipos y Miembros del Equipo.
3. Usa el formulario de búsqueda en la página de inicio para encontrar proyectos por nombre o descripción.

## Pasos de Uso de la Web
Para utilizar la web de manera efectiva, sigue estos pasos en el orden indicado:

### Crear un Equipo:
1. Ve a la sección "Equipos".
2. Llena el formulario para agregar un nuevo equipo con su nombre y descripción.
3. Guarda el equipo.

### Agregar Miembros al Equipo:
1. Ve a la sección "Miembros del Equipo".
2. Llena el formulario para agregar nuevos miembros al equipo, incluyendo su nombre, apellido, rol y el equipo al que pertenecen.
3. Guarda los miembros del equipo.

### Crear un Proyecto:
1. Ve a la sección "Proyectos".
2. Llena el formulario para agregar un nuevo proyecto, incluyendo el nombre, descripción, fecha de inicio y fecha de finalización.
3. Guarda el proyecto.

### Agregar Tareas al Proyecto:
1. Ve a la sección "Tareas".
2. Llena el formulario para agregar nuevas tareas, incluyendo el nombre, descripción, proyecto al que pertenece, fecha de inicio, fecha de finalización y estado.
3. Guarda las tareas.

### Buscar Proyectos:
1. Ve a la página de inicio.
2. Utiliza el formulario de búsqueda para encontrar proyectos por nombre o descripción.


## Orden de Pruebas

1. Inicio: Realiza una búsqueda de proyectos.
2. Proyectos: Agrega nuevos proyectos y visualiza la lista de proyectos.
3. Tareas: Agrega nuevas tareas y visualiza la lista de tareas.
4. Equipos: Agrega nuevos equipos y visualiza la lista de equipos.
5. Miembros del Equipo: Agrega nuevos miembros al equipo y visualiza la lista de miembros.

## Funcionalidades

- Herencia de HTML con plantillas base.
- Cuatro modelos: Proyecto, Tarea, Equipo y MiembroEquipo.
- Formularios para agregar datos a cada modelo.
- Formulario de búsqueda en la página de inicio.




