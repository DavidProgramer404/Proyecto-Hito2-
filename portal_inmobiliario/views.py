from django.shortcuts import render
from django.http import HttpResponse
from portal_app.models import *
from portal_app.services import *

def index(request):
    tipo_u = get_usuarios()
    context ={'tipo_u':tipo_u}
    return render(request,'index.html',context)
