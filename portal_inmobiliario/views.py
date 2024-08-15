from django.shortcuts import render, redirect
from django.http import HttpResponse
from portal_app.models import *
from portal_app.services import *


def index(request):
    # Consulta SQL cruda para obtener todos los usuarios
    sql = 'SELECT * FROM usuarios'
    
    # Ejecuta la consulta cruda
    usuarios = Usuario.objects.raw(sql)
    
    # Pasa los usuarios al contexto de la plantilla
    context = {'usuarios': usuarios}
    return render(request, 'base.html', context)

# arrendatario

def perfil_arrendatario(request):
    # Consulta SQL cruda para obtener todos los arrendatarios
    sql = 'SELECT * FROM usuarios WHERE id_tipo_usuario = (SELECT id_tipo_usuario FROM tipo_usuarios WHERE tipo_usuario = "Arrendatario")'
    
    # Ejecuta la consulta cruda
    arrendatarios = Usuario.objects.raw(sql)
    
    # Pasa los arrendatarios al contexto de la plantilla
    context = {'arrendatarios': arrendatarios}
    return render(request, 'portal_app/perfil_arrendatario.html', context)