# Create your views here.
from django.shortcuts import render
from .models import Mascota

def dashboard(request):
    # Traemos todas las mascotas de la base de datos
    mascotas = Mascota.objects.all()
    # Las enviamos al archivo HTML
    return render(request, 'index.html', {'mascotas': mascotas})