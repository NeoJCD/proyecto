from django.db import models
from django.contrib.auth.models import User

# Tabla de Perfiles (Cargos)
class PerfilEmpleado(models.Model):
    OPCIONES_CARGO = [
        ('TECNICO', 'Técnico de Campo'),
        ('SEGURIDAD', 'Seguridad Física'),
        ('ADMIN', 'Administrador/Gerente'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=20, choices=OPCIONES_CARGO, default='TECNICO')

    def __str__(self):
        return f"{self.usuario.username} - {self.cargo}"

class Pozo(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100, default="Sin ubicación asignada") 
    barriles_diarios = models.DecimalField(max_digits=10, decimal_places=2)
    profundidad_metros = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default="Operativo") 

    def __str__(self):
        return self.nombre