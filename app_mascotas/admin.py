# Register your models here.
from django.contrib import admin
from django.db import models
from django import forms
from .models import Mascota, RegistroMedico, Suscripcion

# Forzamos el uso del calendario moderno de HTML5
class MascotaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': forms.DateInput(attrs={'type': 'date'})},
    }

class RegistroMedicoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': forms.DateInput(attrs={'type': 'date'})},
    }

class SuscripcionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': forms.DateInput(attrs={'type': 'date'})},
    }

# Registramos TODOS los modelos con su nueva configuración
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(RegistroMedico, RegistroMedicoAdmin)
admin.site.register(Suscripcion, SuscripcionAdmin)