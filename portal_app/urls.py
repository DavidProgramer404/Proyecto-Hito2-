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
    path('perfil_arrendatario/', views.perfil_arrendatario, name='perfil_arrendatario'),
    path('perfil_arrendador/', views.perfil_arrendador, name='perfil_arrendador'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_inmueble/', views.crear_inmueble, name='crear_inmueble'),
    path('register/', views.register, name='register'),
    
]
