from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, InmuebleForm, LoginForm
from .models import Inmueble, Usuario

# Vista principal (Página de inicio)
def index(request):
    return render(request, 'index.html')

# Vista para crear un nuevo usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'portal_app/crear_usuario.html', {'form': form})

# Vista para registrar un nuevo usuario (autenticación)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Vista para el perfil del arrendatario
@login_required
def perfil_arrendatario(request):
    usuario = request.user
    return render(request, 'portal_app/perfil_arrendatario.html', {'usuario': usuario})

# Vista para el perfil del arrendador
@login_required
def perfil_arrendador(request):
    usuario = request.user
    return render(request, 'portal_app/perfil_arrendador.html', {'usuario': usuario})

# Vista para el perfil de arrendatarios (lista de arrendatarios)
@login_required
def perfil_arrendatarios(request):
    arrendatarios = Usuario.objects.filter(tipo_usuario='arrendatario')
    return render(request, 'portal_app/perfil_arrendatarios.html', {'arrendatarios': arrendatarios})

# Vista para crear un nuevo inmueble
@login_required
def crear_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portal_app/inmuebles_list')
    else:
        form = InmuebleForm()
    return render(request, 'portal_app/crear_inmueble.html', {'form': form})

# Vista para actualizar un inmueble existente
@login_required
def actualizar_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id_inmueble=inmueble_id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('inmuebles_list')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'portal_app/actualizar_inmueble.html', {'form': form})

# Vista para listar inmuebles
@login_required
def inmuebles_list(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'portal_app/inmuebles_list.html', {'inmuebles': inmuebles})

# Vista para ver un inmueble específico
@login_required
def ver_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'portal_app/ver_inmuebles.html', {'inmuebles': inmuebles})

# Vista para agregar un nuevo inmueble
@login_required
def agregar_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portal_app/inmuebles_list')
    else:
        form = InmuebleForm()
    return render(request, 'portal_app/crear_inmueble.html', {'form': form})

# Vista para borrar un inmueble existente
@login_required
def borrar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, id=id)
    inmueble.delete()
    return redirect('portal_app/borrar_inmuebles.html')
