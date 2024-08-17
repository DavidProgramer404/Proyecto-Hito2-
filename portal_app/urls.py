from django.urls import path,include
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    # logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_inmueble/', views.crear_inmueble, name='crear_inmueble'),
    path('actualizar_inmueble/<int:inmueble_id>/', views.actualizar_inmueble, name='actualizar_inmueble'),
    path('register/', views.register, name='register'),
    # path('logout/', views.logout_view, name='logout'),
    path('perfil_arrendatario/', views.perfil_arrendatario, name='perfil_arrendatario'),
    path('perfil_arrendador/', views.perfil_arrendador, name='perfil_arrendador'),
    path('perfil_arrendatarios/', views.perfil_arrendatarios, name='perfil_arrendatarios'),
    path('inmuebles_list/', views.inmuebles_list, name='inmuebles_list'),
    path('ver_inmuebles/', views.ver_inmuebles, name='ver_inmuebles'),
    
]
