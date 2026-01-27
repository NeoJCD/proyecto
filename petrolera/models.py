from django.db import models
from django.contrib.auth.models import User

# 1. PERFIL DE EMPLEADO (Para saber quién es quién)
class PerfilEmpleado(models.Model):
    ROLES = [
        ('TECNICO', 'Técnico de Campo'),    # Acceso a Producción/Perforación
        ('ADMIN', 'Administrativo'),        # Acceso a Contabilidad
        ('SEGURIDAD', 'Seguridad'),         # Acceso a Áreas Seguras
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.usuario.username} - {self.cargo}"

# 2. NIVEL TÉCNICO: Datos de Pozos (Producción y Perforación)
class Pozo(models.Model):
    nombre = models.CharField(max_length=100)
    barriles_diarios = models.IntegerField()
    profundidad_metros = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default="Operativo")

    def __str__(self):
        return self.nombre

# 3. NIVEL ADMINISTRATIVO: Datos Contables (Facturas)
class Factura(models.Model):
    cliente = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    pagada = models.BooleanField(default=False)

# 4. NIVEL SEGURIDAD: Reporte de Áreas
class AreaSegura(models.Model):
    nombre_zona = models.CharField(max_length=100)
    nivel_acceso = models.IntegerField(default=1)
    ultima_revision = models.DateTimeField(auto_now=True)
    es_segura = models.BooleanField(default=True)