from django.db import models


# 📁 Modelo para Proyectos
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre  # Representa el objeto con su nombre


# 📁 Modelo para Equipos
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


# 👥 Modelo para Miembros del Equipo
class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rol = models.CharField(max_length=100)
    equipo = models.ForeignKey(
        Equipo, on_delete=models.CASCADE
    )  # Relación con el equipo

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# 📋 Modelo para Tareas
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE
    )  # Relación con el proyecto
    equipo = models.ForeignKey(
        Equipo, on_delete=models.CASCADE, default=1
    )  # Relación con el equipo (asumiendo que el ID 1 corresponde a un equipo existente)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=[
            ("Pendiente", "Pendiente"),
            ("En progreso", "En progreso"),
            ("Completada", "Completada"),
        ],
    )

    def __str__(self):
        return self.nombre
