from django.shortcuts import render, redirect
from .models import Usuario, Inmueble
from .forms import UsuarioForm, InmuebleForm
from django.db import models
from portal_app.models import Usuario

def index(request):
    usuarios = Usuario.objects.all()
    inmuebles = Inmueble.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios, 'inmuebles': inmuebles})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'portal_app/crear_usuario.html', {'form': form})

def crear_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            Inmueble = form.save(commit=False)
            Inmueble.usuario = request.user
            form.save()
            return redirect('inmuebles_list')
    else:
        form = InmuebleForm()
    return render(request, 'portal_app/crear_inmueble.html', {'form': form})

# login
def login(request):
    return render(request, 'portal_app/login.html')

# register
def register(request):
    return render(request, 'portal_app/register.html')

# logout
def logout(request):
    return redirect('login')

# perfil_arrendatario
def perfil_arrendatario(request):
    return render(request, 'portal_app/perfil_arrendatario.html')

# perfil_arrendador
def perfil_arrendador(request):
    # Lógica de la vista de perfil del arrendador
    return render(request, 'portal_app/perfil_arrendador.html')