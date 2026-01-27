from django.contrib import admin
from django.urls import path, include
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tareas.urls')), 
    path('api/petrolera/', include('petrolera.urls')),
    path('api-auth/', include('rest_framework.urls')),
]