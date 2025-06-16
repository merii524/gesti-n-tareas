Resumen Checklist
Crear entorno virtual e instalar dependencias.

Crear proyecto y app.

Definir el modelo de tarea con campo completed.

Migrar la base de datos.

Crear vistas para listar, crear y actualizar tareas.

Implementar lógica para cambiar el estado de las tareas.

Filtrar y mostrar tareas según su estado.

Mejorar la interfaz y seguridad según necesidades.t

#Instala dependencias
pip intall -r requirements.txt

#Creacion de proyecto django
django-admin startproject proyectoFinalProgramacionAvanzada

#Creacion de app Tareas
python manage.py startapp tareas

#Se configura la vista
#Se configura la urls, en la app tareas
#Se configura la urls, en el proyecto
#Se agrega INSTALLED_APPS = [
    'tareas.apps.TareasConfig'
    ...
    ...
    ]

#Se configura la base de datos
#Este comando crea las tablas de las base de datos que utilize por defecto django
python manage.py migrate

#se crea el modelo de tareas

# Definición del modelo Tarea
# Este modelo representa una tarea en la aplicación de gestión de tareas
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

Este comando es para avisar que realizaste algunos cambios en los modelos, y los cambios de almacenen como una migración 
#py manage.py makemigrations tareas
#Con este comando realiza la migración y aplica los cambios
#py manage.py migrate

#Jugando con la base de datos en la consola
python manage.py shell
 import tareas.models import Tarea 
t = Tarea(titulo="Aprende django",descripcion="seguir tutorial",completada=False)
t.save()

#Listar todas las tareas
Tarea.objects.all()


#Filtrar tarea por estado
# Tareas completadas
Task.objects.filter(completed=True)
# Tareas pendientes
Task.objects.filter(completed=False)

#Buscar por id
Tarea.objects.get(pk=1)

#Eliminar tareea
t = Tarea.objects.get(pk=1)
t.delete()

#Creando un usuario administrador
py manage.py createsuperuser

user=admin
password=1234

#Se crea la administracion de tareas atraves del modelo
#Se muestra la lista de las tareas que hay en la base de datos, y se puede editar
#Tareas/Admin.py
from .models import Tarea
admin.site.register(Tarea)
