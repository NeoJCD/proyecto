from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Pozo, PerfilEmpleado 

# --- 1. SERIALIZER DE POZOS ---
class PozoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pozo
        fields = '__all__'

# --- 2. SERIALIZER DE REGISTRO DE USUARIOS ---
class RegistroUsuarioSerializer(serializers.ModelSerializer):
    cargo = serializers.ChoiceField(choices=PerfilEmpleado.OPCIONES_CARGO, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'cargo']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        cargo_elegido = validated_data.pop('cargo')
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password) 
        user.save()

    
        PerfilEmpleado.objects.create(usuario=user, cargo=cargo_elegido)
        
        return user

