# petrolera/cookies.py
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            # 1. Ejecutamos el login normal de JWT
            response = super().post(request, *args, **kwargs)
            
            if response.status_code != status.HTTP_200_OK:
                return response
                
            tokens = response.data
            
            # 2. Configuración de Cookies (ACCESS TOKEN)
            response.set_cookie(
                key="access_token", # Nombre de la cookie
                value=tokens['access'],
                httponly=True,      # JavaScript no puede leerla (Seguridad XSS)
                secure=False,       # Ponlo en True si usas HTTPS en producción
                samesite='Lax',     
                path='/',
                max_age=3600        # Expira en 1 hora
            )
            
            # 3. Configuración de Cookies (REFRESH TOKEN)
            response.set_cookie(
                key="refresh_token",
                value=tokens['refresh'],
                httponly=True,
                secure=False,
                samesite='Lax',
                path='/',
                max_age=3600 * 24 * 7 # Expira en 7 días
            )
            
            return response
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            # 1. Buscamos el refresh token en la cookie si no viene en el body
            refresh_token = request.COOKIES.get('refresh_token')
            
            if refresh_token:
                request.data['refresh'] = refresh_token
                
            response = super().post(request, *args, **kwargs)
            
            if response.status_code != status.HTTP_200_OK:
                return response
                
            # 2. Actualizamos la cookie del Access Token
            response.set_cookie(
                key="access_token",
                value=response.data['access'],
                httponly=True,
                secure=False,
                samesite='Lax',
                path='/',
                max_age=3600
            )
            
            return response
            
        except Exception as e:
            return Response({'error': 'Token invalido o expirado'}, status=status.HTTP_401_UNAUTHORIZED)