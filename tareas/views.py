from django.shortcuts import render,redirect,get_object_or_404
from .models import Tarea as Tarea
from django import forms
# Formulario para crear una tarea
class TareaForm(forms.ModelForm):
    class Meta:
        """Clase Meta para definir el modelo y los campos del formulario."""
        # Esta clase se utiliza para especificar el modelo y los campos que se incluirán en el formulario.
        # Permite que el formulario se genere automáticamente a partir del modelo Tarea.
        model = Tarea
        fields = ['titulo', 'descripcion']

def crear_tarea(request):
    """Crea una nueva instancia del modelo Tarea utilizando un formulario.
    Si la solicitud es POST, valida los datos del formulario y guarda la nueva tarea."""
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear_tarea.html', {'form': form})


def listar_tareas(request):
    """Obtiene todas las instancias del modelo Tarea y las pasa al template 'tareas/listar_tareas.html'
    para mostrar la lista completa de tareas al usuario.
    Parámetros:
        request (HttpRequest): Objeto que contiene la información de la solicitud HTTP.
    Retorna:
        HttpResponse: Renderiza la plantilla con el contexto que incluye todas las tareas."""
    tareas = Tarea.objects.all()
    return render(request, 'tareas/listar_tareas.html', {'tareas': tareas})

def detalle_tarea(request, tarea_id):
    """Obtiene una tarea específica por su ID o retorna un error 404 si no existe.
    Luego renderiza el template 'tareas/detalle_tarea.html' mostrando la información detallada de la tarea.
    Parámetros:
        request (HttpRequest): Objeto que contiene la información de la solicitud HTTP.
        tarea_id (int): Identificador único de la tarea a mostrar.
    Retorna:
        HttpResponse: Renderiza la plantilla con el contexto que incluye la tarea solicitada """
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})

def cambiar_estado_tarea(request, tarea_id):
    """ Cambia el estado booleano 'completada' de una tarea específica (de True a False o viceversa).
    Luego guarda los cambios y redirige a la vista de detalle de la tarea para mostrar el estado actualizado.
    Parámetros:
        request (HttpRequest): Objeto que contiene la información de la solicitud HTTP.
        tarea_id (int): Identificador único de la tarea cuyo estado se modificará.
    Retorna:
        HttpResponseRedirect: Redirige a la vista 'detalle_tarea' para mostrar la tarea actualizada."""
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    tarea.completada = not tarea.completada 
    tarea.save()
    return redirect('detalle_tarea', tarea_id=tarea.id)

def eliminar_tarea(request, tarea_id):
    """
    Elimina una tarea específica identificada por su ID y redirige a la lista de tareas.
    """
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    tarea.delete()
    return redirect('listar_tareas')


def editar_tarea(request, tarea_id):
    """
    Vista para editar una tarea existente.
    Carga los datos actuales en el formulario y guarda los cambios tras validación.
    """
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('detalle_tarea', tarea_id=tarea.id)
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'tareas/editar_tarea.html', {'form': form, 'tarea': tarea})