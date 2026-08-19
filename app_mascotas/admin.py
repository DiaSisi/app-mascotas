# Register your models here.
from django.contrib import admin
from .models import Mascota, RegistroMedico, Suscripcion

admin.site.register(Mascota)
admin.site.register(RegistroMedico)
admin.site.register(Suscripcion)