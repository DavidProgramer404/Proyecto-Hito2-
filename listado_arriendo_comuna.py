import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_inmobiliario.settings')
django.setup()

from portal_app.models import Inmueble

def inmuebles_part2():
    # Realiza la consulta
    inmuebles = Inmueble.objects.select_related('id_comuna').values('id_comuna__comuna', 'nombre', 'descripcion').order_by('id_comuna__comuna')

    # Organiza los inmuebles por comuna
    comunas_dict = {}
    for inmueble in inmuebles:
        comuna = inmueble['id_comuna__comuna']
        if comuna not in comunas_dict:
            comunas_dict[comuna] = []
        comunas_dict[comuna].append(f"{inmueble['nombre']} - {inmueble['descripcion']}")

    # Guarda los resultados en un archivo de texto
    with open('inmuebles_por_comuna.txt', 'w',encoding='utf-8') as file:
        for comuna, inmuebles_list in comunas_dict.items():
            file.write(f"Comuna: {comuna}\n")
            for inmueble in inmuebles_list:
                file.write(f"  {inmueble}\n")
            file.write("\n")

if __name__ == "__main__":
    inmuebles_part2()
