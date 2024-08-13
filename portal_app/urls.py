from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('perfil_arrendatario/', views.perfil_arrendatario, name='perfil_arrendatario'),
    path('perfil_arrendador/', views.perfil_arrendador, name='perfil_arrendador'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_inmueble/', views.crear_inmueble, name='crear_inmueble'),
]
