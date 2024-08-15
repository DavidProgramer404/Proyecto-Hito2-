from django.contrib import admin

# Register your models here.
from .models import TipoUsuario

admin.site.register(TipoUsuario)


# Register your models here.
from.models import Inmueble

admin.site.register(Inmueble)

# Register your models here.
from.models import Comuna

admin.site.register(Comuna)

# Register your models here.
from.models import Region

admin.site.register(Region)

# arrendatario
from.models import Usuario

admin.site.register(Usuario)

