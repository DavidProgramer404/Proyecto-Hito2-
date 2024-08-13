from django import forms
from .models import Usuario, Comuna, TipoInmueble, Inmueble

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "nombre",
            "apellido",
            "rut",
            "direccion",
            "telefono_personal",
            "correo_electronico",
            "tipo_usuario",
        ]

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre',
            'm2_construido',
            'm2_terreno',
            'nro_estacionamiento',
            'nro_habitacion',
            'nro_banio',
            'direccion',
            'region',
            'comuna',
            'tipo_inmueble',
            'precio_mensual_arriendo',
            'descripcion',
        ]