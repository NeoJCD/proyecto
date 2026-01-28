from django.contrib import admin
from django.urls import path, include

# Importamos TUS vistas nuevas desde 'petrolera.cookies'
from petrolera.cookies import CustomTokenObtainPairView, CustomRefreshTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/petrolera/', include('petrolera.urls')),
    
    # Rutas de Autenticación Modificadas (Cookies)
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
]