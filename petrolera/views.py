from django.shortcuts import render
from rest_framework import viewsets
# Importamos el permiso personalizado que creaste en el paso anterior
from .permissions import EsTecnicoOAdmin 
from .models import Pozo
from .serializers import PozoSerializer

# --- VISTA PARA EL FRONTEND (HTML) ---
def home(request):
    return render(request, 'index.html')

# --- API DE POZOS (BACKEND) ---
class PozoViewSet(viewsets.ModelViewSet):
    queryset = Pozo.objects.all()
    serializer_class = PozoSerializer
    
    # AQUÍ ESTÁ EL CAMBIO DE SEGURIDAD:
    # Quitamos 'IsAuthenticated' y ponemos nuestro permiso personalizado.
    # Ahora Django verificará si es TECNICO o ADMIN antes de dejarlo pasar.
    permission_classes = [EsTecnicoOAdmin]