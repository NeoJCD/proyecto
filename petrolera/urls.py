from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TecnicoViewSet, AdminViewSet, SeguridadViewSet, UsuarioViewSet # <-- Importa la nueva vista

router = DefaultRouter()
router.register(r'pozos', TecnicoViewSet)
router.register(r'contabilidad', AdminViewSet)
router.register(r'seguridad', SeguridadViewSet)
router.register(r'usuarios', UsuarioViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]