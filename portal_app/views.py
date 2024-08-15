from django.shortcuts import render, redirect
from .models import Usuario, Inmueble
from .forms import UsuarioForm, InmuebleForm
from django.db import models
from portal_app.models import Usuario
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

@login_required
def index(request):
    usuarios = Usuario.objects.all()
    inmuebles = Inmueble.objects.all()
    return render(request, 'base.html', {'usuarios': usuarios, 'inmuebles': inmuebles})

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
# def login(request):
#     return render(request, 'portal_app/login.html')

# register
def register(request):
    return render(request, 'portal_app/register.html')

# logout
# def logout(request):
#     return redirect('login')

# perfil_arrendatario
def perfil_arrendatario(request):
    return render(request, 'portal_app/perfil_arrendatario.html')

# perfil_arrendador
def perfil_arrendador(request):
    # Lógica de la vista de perfil del arrendador
    # Filtrar solo los usuarios que sean arrendadores
    arrendadores = Usuario.objects.filter(tipoUsuario='Arrendador')
    return render(request, 'portal_app/perfil_arrendador.html', {'arrendadores': arrendadores})


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect('index')  # Redirige a la página de inicio o dashboard
#         else:
#             messages.error(request, 'Nombre de usuario o contraseña incorrectos')
#     return render(request, 'portal_app/login.html')

# def logout_view(request):
#     auth_logout(request)
#     return redirect('login')

@login_required
def perfil_arrendatarios(request):
    arrendatarios = Usuario.objects.filter(id_tipo_usuario__tipo_usuario='Arrendatario')
    return render(request, 'portal_app/perfil_arrendatarios.html', {'arrendatarios': arrendatarios})

@login_required
def perfil_arrendador(request):
    # Filtra usuarios que son arrendadores
    arrendadores = Usuario.objects.filter(tipo_usuario__tipo_usuario='Arrendador')
    
    # Pasa los arrendadores al contexto de la plantilla
    context = {'arrendadores': arrendadores}
    return render(request, 'portal_app/perfil_arrendador.html', context)