from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Mascota(models.Model):
    RAZAS_CHOICES = [
        ('mestiza', 'Mestiza'),
        ('schnauzer', 'Schnauzer'),
        ('golden_retriever', 'Golden Retriever'),
        ('poodle', 'Poodle'),
        ('bulldog', 'Bulldog'),
        ('pug', 'Pug'),
        ('pastor_aleman', 'Pastor Alemán'),
        ('otra', 'Otra'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100, choices=RAZAS_CHOICES, default='mestiza')
    fecha_nacimiento = models.DateField()
    peso_actual = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso en kg")

    def __str__(self):
        return self.nombre

class RegistroMedico(models.Model):
    TIPO_CHOICES = [
        ('vacuna', 'Vacuna'),
        ('desparasitante', 'Desparasitante'),
    ]
    
    VACUNAS_CHOICES = [
        ('rabia', 'Rabia'),
        ('sextuple', 'Séxtuple'),
        ('kc', 'KC (Tos de Perrera)'),
        ('otra', 'Otra'),
        ('no_aplica', 'No aplica (Es desparasitante)'),
    ]
    
    DESPARASITANTE_CHOICES = [
        ('interno', 'Interno'),
        ('externo', 'Externo'),
        ('ambos', 'Ambos'),
        ('no_aplica', 'No aplica (Es vacuna)'),
    ]

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    
    # Las nuevas listas desplegables
    vacuna = models.CharField(max_length=50, choices=VACUNAS_CHOICES, default='no_aplica')
    tipo_desparasitante = models.CharField(max_length=20, choices=DESPARASITANTE_CHOICES, default='no_aplica')
    
    # Tu campo original, pero ahora le ponemos blank=True para que sea opcional llenarlo
    # por si el profesor solo selecciona la vacuna y no quiere escribir la marca.
    nombre_medicamento = models.CharField(max_length=100, blank=True, null=True, help_text="Ej: Nexgard, Bravecto. (Opcional)")
    
    # Tus fechas originales intactas
    fecha_aplicacion = models.DateField()
    proxima_fecha = models.DateField()

    # ¡Tu regla de negocio de oro!
    def clean(self):
        super().clean()
        if self.fecha_aplicacion and self.proxima_fecha:
            if self.proxima_fecha <= self.fecha_aplicacion:
                raise ValidationError({
                    'proxima_fecha': 'La próxima fecha sugerida no puede ser anterior ni igual a la fecha de aplicación actual.'
                })

    def __str__(self):
        # Un pequeño ajuste para que muestre el nombre bonito en el panel
        return f"{self.get_tipo_display()} - {self.mascota.nombre}"

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