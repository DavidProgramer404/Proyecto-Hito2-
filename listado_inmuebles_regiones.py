import os
import django

# Configura el entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal_inmobiliario.settings")
django.setup()

# Importa los modelos
from portal_app.models import Region, Comuna, Inmueble

def inmuebles_por_region_part3():
    # Abre un archivo para escribir los datos
    with open('inmuebles_por_region.txt', 'w', encoding='utf-8') as file:
        # Escribe los encabezados
        file.write("Listado de inmuebles para arriendo separado por regiones \n")
        file.write("=" * 80 + "\n")
        
        # Realiza una consulta para obtener todas las regiones
        regiones = Region.objects.all()

        # Itera sobre cada región
        for region in regiones:
            # Escribe el nombre de la región
            file.write(f"Región: {region.region}\n")
            file.write("-" * 80 + "\n")
            
            # Realiza una consulta para obtener todas las comunas de la región actual
            comunas = Comuna.objects.filter(region=region)
            
            # Itera sobre cada comuna
            for comuna in comunas:
                # Realiza una consulta para obtener todos los inmuebles de la comuna actual
                inmuebles = Inmueble.objects.filter(id_comuna=comuna.id_comuna)
                
                # Itera sobre cada inmueble y escribe sus datos en el archivo
                for inmueble in inmuebles:
                    file.write(f"{region.region}\t{inmueble.nombre}\t{inmueble.descripcion}\n")
            
            # Escribe una línea de separación entre regiones
            file.write("=" * 80 + "\n")

    print("Datos guardados en inmuebles_por_region.txt")

if __name__ == "__main__":
    inmuebles_por_region_part3()
