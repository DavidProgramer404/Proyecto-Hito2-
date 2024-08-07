import os
import django

# Configura el entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal_inmobiliario.settings")
django.setup()

# Importa el modelo
from portal_app.models import TipoInmueble

# Realiza una consulta para obtener todos los registros
tipos_inmuebles = TipoInmueble.objects.all()

# Abre un archivo para escribir los datos
with open('tipo_inmueble.txt', 'w') as file:
    # Escribe los encabezados
    file.write("id_tipo_inmueble\t tipo_inmueble\n")
    file.write("-" * 40 + "\n")
    
    # Escribe los datos
    for tipo in tipos_inmuebles:
        file.write(f"{tipo.id_tipo_inmueble}\t {tipo.tipo_inmueble}\n")

print("Datos guardados en tipo_inmueble.txt")
