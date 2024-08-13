from django.shortcuts import render
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
    return render(request, 'index.html', context)