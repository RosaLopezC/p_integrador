from django.urls import path
from . import views  # Importar las vistas desde el archivo views.py

urlpatterns = [
    path('', views.login_view, name='login'),  # Ruta para la página de inicio de sesión
    path('registro/', views.registro_view, name='registro'),  # Ruta para el registro
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('menu/', views.menu, name='menu'),
]
