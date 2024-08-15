from django import forms
from .models import Usuario, Comuna, TipoInmueble, Inmueble
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

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


class LoginForm(forms.Form):
    correo_electronico = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo Electrónico',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña',
    }))

    def clean(self):
        correo_electronico = self.cleaned_data.get('correo_electronico')
        password = self.cleaned_data.get('password')
        user = authenticate(username=correo_electronico, password=password)
        if user is None:
            raise forms.ValidationError('Correo electrónico o contraseña incorrectos')
        return self.cleaned_data

    def get_user(self):
        correo_electronico = self.cleaned_data.get('correo_electronico')
        user = authenticate(username=correo_electronico, password=self.cleaned_data.get('password'))
        return user