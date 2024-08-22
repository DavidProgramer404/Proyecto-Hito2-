from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
    # Autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Página de inicio
    path('', index, name='index'),

    # Registro y creación de usuarios
    path('register/', register, name='register'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),

    # Gestión de inmuebles
    path('inmuebles/nuevo/', crear_inmueble, name='crear_inmueble'),
    path('inmuebles/editar/<int:inmueble_id>/', actualizar_inmueble, name='actualizar_inmueble'),
    path('inmuebles/borrar/<int:inmueble_id>/', borrar_inmueble, name='borrar_inmueble'),
    path('inmuebles/lista/', inmuebles_list, name='inmuebles_list'),
    path('inmuebles/ver/', ver_inmuebles, name='ver_inmuebles'),
    path('actualizar_inmueble/<int:inmueble_id>/', views.actualizar_inmueble, name='actualizar_inmueble'),
    

    # Perfiles de usuarios
    path('perfil_arrendatario/', perfil_arrendatario, name='perfil_arrendatario'),
    path('perfil_arrendador/', perfil_arrendador, name='perfil_arrendador'),
    path('perfil_arrendatarios/', perfil_arrendatarios, name='perfil_arrendatarios'),
    
]
