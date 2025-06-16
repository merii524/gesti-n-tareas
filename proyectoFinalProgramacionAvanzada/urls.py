"""
URL configuration for proyectoFinalProgramacionAvanzada project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Configuración de las URLs del proyecto para que incluyan las rutas de la aplicación 'tareas'
# Aquí se definen las rutas principales del proyecto, incluyendo la aplicación 'tareas'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tareas/', include('tareas.urls')),
]
