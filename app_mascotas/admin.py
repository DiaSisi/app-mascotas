# Register your models here.
from django.contrib import admin
from django.db import models
from django import forms
from .models import Mascota, RegistroMedico, Suscripcion

# 1. Creamos un diseño que bloquea el calendario confuso de Jazzmin
class CalendarioModerno(forms.DateInput):
    input_type = 'date'

# 2. Se lo aplicamos a un panel maestro
class PanelMaestro(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': CalendarioModerno(attrs={'class': 'form-control'})},
    }

# 3. Registramos tus 3 tablas usando ese panel maestro
admin.site.register(Mascota, PanelMaestro)
admin.site.register(RegistroMedico, PanelMaestro)
admin.site.register(Suscripcion, PanelMaestro)