from rest_framework import serializers
from .models import Pozo, Factura, AreaSegura

class PozoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pozo
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class AreaSeguraSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaSegura
        fields = '__all__'
from django.contrib.auth.models import User
from .models import PerfilEmpleado 

# --- SERIALIZER DE REGISTRO ---
class RegistroUsuarioSerializer(serializers.ModelSerializer):
    
    cargo = serializers.ChoiceField(choices=PerfilEmpleado.ROLES, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'cargo']

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        cargo_elegido = validated_data.pop('cargo')
        password = validated_data.pop('password')

        #Creamos el usuario base
        user = User(**validated_data)
        user.set_password(password) 
        user.save()

    
        PerfilEmpleado.objects.create(usuario=user, cargo=cargo_elegido)
        
        return user