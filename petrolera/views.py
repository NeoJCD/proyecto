from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import generics
from rest_framework.permissions import AllowAny # <-- Importante importar esto
from rest_framework.permissions import IsAdminUser
from .serializers import RegistroUsuarioSerializer
from django.contrib.auth.models import User
from .models import Pozo, Factura, AreaSegura
from .serializers import PozoSerializer, FacturaSerializer, AreaSeguraSerializer

# --- VISTA TÉCNICOS ---
# Tienen un límite "medio" para consultar pozos
class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Pozo.objects.all()
    serializer_class = PozoSerializer
    permission_classes = [IsAuthenticated]
    
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'tecnicos' 

# --- VISTA ADMINISTRATIVOS ---
# Tienen un límite más estricto (no necesitan consultar tanto)
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated]
    
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'administrativos'

# --- VISTA SEGURIDAD ---
# Necesitan velocidad casi real (límite muy alto)
class SeguridadViewSet(viewsets.ModelViewSet):
    queryset = AreaSegura.objects.all()
    serializer_class = AreaSeguraSerializer
    permission_classes = [IsAuthenticated]
    
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'seguridad'
    # --- VISTA DE REGISTRO (PÚBLICA) ---
class RegistroView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [AllowAny] 

    # --- NUEVO: GESTIÓN DE USUARIOS (CRUD COMPLETO) ---
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [IsAdminUser] 