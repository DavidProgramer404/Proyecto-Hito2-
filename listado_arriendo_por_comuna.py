import os
import django

# Configura el entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal_inmobiliario.settings")
django.setup()

# Importa los modelos
from portal_app.models import Comuna, Inmueble

# Realiza una consulta para obtener todas las comunas
comunas = Comuna.objects.all()

# Abre un archivo para escribir los datos
with open('inmuebles_para_arriendo_por_comuna.txt', 'w', encoding='utf-8') as file:
    # Escribe los encabezados
    file.write("Comuna\tNombre Inmueble\tDescripción\n")
    file.write("=" * 80 + "\n")
    
    # Itera sobre cada comuna
    for comuna in comunas:
        # Escribe el nombre de la comuna
        file.write(f"Comuna: {comuna.comuna}\n")
        file.write("-" * 80 + "\n")
        
        # Realiza una consulta para obtener todos los inmuebles de la comuna actual
        inmuebles = Inmueble.objects.filter(comuna=comuna, tipo='arriendo')
        
        # Itera sobre cada inmueble y escribe sus datos en el archivo
        for inmueble in inmuebles:
            file.write(f"{comuna.comuna}\t{inmueble.nombre}\t{inmueble.descripcion}\n")
        
        # Escribe una línea de separación entre comunas
        file.write("=" * 80 + "\n")

print("Datos guardados en inmuebles_para_arriendo_por_comuna.txt")

