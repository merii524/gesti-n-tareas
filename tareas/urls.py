from django.urls import path

from . import views

# Definición de las URLs para la aplicación tareas
# Aquí se definen las rutas que la aplicación tareas manejará
urlpatterns = [
    # Ruta principal que muestra la lista de tareas
    path('', views.listar_tareas, name='listar_tareas'),
    # Ruta para mostrar el detalle de una tarea específica, identificada por su ID entero
    path('tareas/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    # Ruta para cambiar el estado de completado de una tarea específica, identificada por su ID entero
    path('tareas/<int:tarea_id>/cambiar_estado/', views.cambiar_estado_tarea, name='cambiar_estado_tarea'),
    # Ruta para crear una nueva tarea, que utiliza un formulario
    path('crear/', views.crear_tarea, name='crear_tarea'),
    # Ruta para eliminar una tarea específica, identificada por su ID entero
    path('tareas/<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    # Ruta para editar una tarea específica, identificada por su ID entero
    path('tareas/<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),

]