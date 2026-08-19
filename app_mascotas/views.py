# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Mascota

def dashboard(request):
    # TRUCO: Crear el usuario evaluador automáticamente si no existe en Render
    if not User.objects.filter(username='profesor').exists():
        User.objects.create_superuser('profesor', 'profe@correo.com', 'diplomado123')
        
    mascotas = Mascota.objects.all()
    return render(request, 'index.html', {'mascotas': mascotas})