from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Mascota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    peso_actual = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso en kg")

    def __str__(self):
        return self.nombre

class RegistroMedico(models.Model):
    TIPO_CHOICES = [
        ('vacuna', 'Vacuna'),
        ('desparasitante', 'Desparasitante'),
    ]
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nombre_medicamento = models.CharField(max_length=100)
    fecha_aplicacion = models.DateField()
    proxima_fecha = models.DateField()

    def clean(self):
        super().clean()
        if self.fecha_aplicacion and self.proxima_fecha:
            if self.proxima_fecha <= self.fecha_aplicacion:
                raise ValidationError({
                    'proxima_fecha': 'La próxima fecha sugerida no puede ser anterior ni igual a la fecha de aplicación actual.'
                })

    def __str__(self):
        return f"{self.tipo} - {self.nombre_medicamento} ({self.mascota.nombre})"

class Suscripcion(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    mascota = models.OneToOneField(Mascota, on_delete=models.CASCADE)
    numero_poliza = models.CharField(max_length=50, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Póliza {self.numero_poliza} - {self.mascota.nombre}"