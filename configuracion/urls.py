from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea conecta tu proyecto con tu app "tareas":
    path('', include('tareas.urls')), 
]