# petrolera/customtoken.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # --- ADAPTACIÓN A TU PROYECTO ---
        # Intentamos obtener el cargo desde PerfilEmpleado
        try:
            cargo_usuario = user.perfilempleado.cargo
        except:
            cargo_usuario = "SIN_CARGO"

        # Agregamos datos extra dentro del token encriptado
        token['email'] = user.email
        token['cargo'] = cargo_usuario  # Antes era 'role'
        
        return token
        
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Intentamos obtener el cargo nuevamente para la respuesta JSON
        try:
            cargo_usuario = self.user.perfilempleado.cargo
        except:
            cargo_usuario = "SIN_CARGO"

        # Datos visibles en el JSON de respuesta
        data['user_id'] = self.user.id
        data['user_name'] = self.user.username
        data['cargo'] = cargo_usuario
        
        return data