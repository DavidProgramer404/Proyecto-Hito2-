import os
import django

# Configura el entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal_inmobiliario.settings")
django.setup()

# Importa los modelos
from portal_app.models import Region, Comuna, Inmueble

# Realiza una consulta para obtener todos los registros de regiones
regiones = Region.objects.all()

# Abre un archivo para escribir los datos
with open('inmuebles_para_arriendo.txt', 'w', encoding='utf-8') as file:
    # Escribe los encabezados
    file.write("Región\tComuna\tNombre Inmueble\tDescripción\n")
    file.write("=" * 80 + "\n")
    
    # Itera sobre cada región
    for region in regiones:
        # Escribe el nombre de la región
        # file.write(f"{region.region}\n")
        file.write("-" * 80 + "\n")
        
        # Itera sobre cada comuna de la región
        comunas = Comuna.objects.filter(region=region.id_region)
        for comuna in comunas:
            # file.write(f"{comuna.comuna}\n")
            # Realiza una consulta para obtener todos los inmuebles de la comuna actual
            # inmuebles = Inmueble.objects.filter(id_comuna=comuna.id_comuna).filter(tipo='arriendo')
            inmuebles = Inmueble.objects.filter(id_comuna=comuna.id_comuna).filter(id_tipo_inmueble=2)
            
            # Itera sobre cada inmueble y escribe sus datos en el archivo
            for inmueble in inmuebles:
                # file.write(f"{region.region}\t{comuna.comuna}\t{inmueble.nombre}\t{inmueble.descripcion}\n")
                file.write(f"{inmueble}\t | {inmueble.descripcion}\n")
        
        # Escribe una línea de separación entre regiones
        file.write("=" * 80 + "\n")

print("Datos guardados en inmuebles_para_arriendo.txt")
