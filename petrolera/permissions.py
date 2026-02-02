from rest_framework import permissions

class EsTecnicoOAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # 1. Primero: ¿Está logueado?
        if not request.user.is_authenticated:
            return False
            
        # 2. Segundo: ¿Tiene el cargo correcto?
        try:
            cargo = request.user.perfilempleado.cargo
            # Solo dejamos pasar si es TECNICO o ADMIN
            if cargo in ['TECNICO', 'ADMIN']:
                return True
            return False
        except:
            # Si no tiene perfil o falla algo, bloqueamos el paso
            return False