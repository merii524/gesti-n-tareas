from django.db import models

# Definición del modelo Tarea
# Este modelo representa una tarea en la aplicación de gestión de tareas
class Tarea(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
