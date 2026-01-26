from django.urls import path
from . import views 

urlpatterns = [
    path('prueba-limite/', views.vista_limitada, name='prueba_limite'),
]