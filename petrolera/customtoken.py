from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        try:
            cargo_usuario = user.perfilempleado.cargo
        except:
            cargo_usuario = "SIN_CARGO"
        token['cargo'] = cargo_usuario
        return token
        
    def validate(self, attrs):
        data = super().validate(attrs)
        try:
            cargo_usuario = self.user.perfilempleado.cargo
        except:
            cargo_usuario = "SIN_CARGO"
        data['user_name'] = self.user.username
        data['cargo'] = cargo_usuario
        return data