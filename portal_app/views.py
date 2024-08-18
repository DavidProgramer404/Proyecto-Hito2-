from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Inmueble
from .forms import UsuarioForm, InmuebleForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

@login_required
def index(request):
    usuarios = Usuario.objects.all()
    usuario = request.user
    inmuebles = Inmueble.objects.all()
    return render(request, 'base.html', {'usuarios': usuarios, 'inmuebles': inmuebles,'usuario': usuario})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'portal_app/crear_usuario.html', {'form': form})

@login_required
def crear_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.usuario = request.user.usuario  # Asumimos que Usuario está relacionado con el User
            inmueble.save()
            return redirect('inmuebles_list')
    else:
        form = InmuebleForm()
    return render(request, 'portal_app/crear_inmueble.html', {'form': form})

@login_required
def actualizar_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id, usuario=request.user.usuario)
    
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('inmuebles_list')
    else:
        form = InmuebleForm(instance=inmueble)
    
    return render(request, 'portal_app/actualizar_inmueble.html', {'form': form, 'inmueble': inmueble})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    return render(request, 'portal_app/register.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def perfil_arrendatario(request):
    return render(request, 'portal_app/perfil_arrendatario.html')

@login_required
def perfil_arrendador(request):
    arrendadores = Usuario.objects.filter(tipo_usuario__tipo_usuario='Arrendador')
    context = {'arrendadores': arrendadores}
    return render(request, 'portal_app/perfil_arrendador.html', context)

@login_required
def perfil_arrendatarios(request):
    arrendatarios = Usuario.objects.filter(tipo_usuario__tipo_usuario='Arrendatario')
    return render(request, 'portal_app/perfil_arrendatarios.html', {'arrendatarios': arrendatarios})

@login_required
def inmuebles_list(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'portal_app/inmuebles_list.html', {'inmuebles': inmuebles})

@login_required
def ver_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'portal_app/ver_inmuebles.html', {'inmuebles': inmuebles})
    # return render(request, 'portal_app/ver_inmuebles.html', {'inmuebles': inmuebles})


# REGISTER
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Crear un nuevo usuario
        user = User.objects.create_user(username=username, password=password)
        # Autenticar y loguear al nuevo usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('index')  # Redirige a la página de inicio o dashboard
        else:
            messages.error(request, 'Error en el registro.')
    return render(request, 'registration/register.html')