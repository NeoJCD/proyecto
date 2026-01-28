from django.contrib import admin
from django.urls import path, include

# 1. IMPORTAMOS LAS VISTAS DEL VIDEO
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/petrolera/', include('petrolera.urls')),
    path('api-auth/', include('rest_framework.urls')), # Login botón azul (opcional)

    # 2. RUTAS DE TOKENS (Tal cual el video)
    # Esta es para hacer LOGIN y obtener el token:
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Esta es para refrescar el token cuando caduca:
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]