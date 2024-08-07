import os
import django

# Configura el entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal_inmobiliario.settings")
django.setup()

# Importa el modelo
from portal_app.models import Comuna

# Realiza una consulta para obtener todos los registros
comunas = Comuna.objects.all()

# Abre un archivo para escribir los datos
with open('comunas.txt', 'w') as file:
    # Escribe los encabezados
    file.write("id_comuna\t comuna\n")
    file.write("-" * 40 + "\n")
    
    # Escribe los datos
    for comuna in comunas:
        file.write(f"{comuna.id_comuna}\t {comuna.comuna}\n")

print("Datos guardados en comunas.txt")
