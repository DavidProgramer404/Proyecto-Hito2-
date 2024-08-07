import os
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal_inmobiliario.settings")
django.setup()
from portal_app.models import TipoUsuario,Comuna,Region,TipoInmueble,Usuario,Inmueble
#como puedo hacer una consulta raw en django
#https://docs.djangoproject.com/en/3.1/topics/db/sql/
# como puedo correr un script en django

#como puedo hacer un loaddata en django
#https://docs.djangoproject.com/en/3.1/howto/initial-data/
