from django import forms
from .models import Inmueble, Usuario
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

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
            # "tipo_usuario",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_personal': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
        }

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
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'm2_construido': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2_terreno': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_estacionamiento': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_habitacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_banio': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-control'}),
            'precio_mensual_arriendo': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

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
        cleaned_data = super().clean()
        correo_electronico = cleaned_data.get('correo_electronico')
        password = cleaned_data.get('password')
        user = authenticate(username=correo_electronico, password=password)
        if user is None:
            raise forms.ValidationError('Correo electrónico o contraseña incorrectos')
        return cleaned_data

    def get_user(self):
        correo_electronico = self.cleaned_data.get('correo_electronico')
        user = authenticate(username=correo_electronico, password=self.cleaned_data.get('password'))
        return user
