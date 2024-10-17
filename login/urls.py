from django.urls import path
from . import views  # Importar las vistas desde el archivo views.py

urlpatterns = [
    path('', views.login_view, name='login'),  # Ruta para la página de inicio de sesión
    path('registro/', views.registro_view, name='registro'),  # Ruta para el registro
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('menu/', views.menu, name='menu'),
    path('numeros/', views.numeros_view, name='numeros'),
    path('sumas_restas/', views.sumas_restas_view, name='sumas_restas'),
    path('secuencias/', views.secuencias_view, name='secuencias'),
    path('geometria/', views.geometria_view, name='geometria'),
    path('medidas/', views.medidas_view, name='medidas'),
    path('fracciones/', views.fracciones_view, name='fracciones'),
    path('multiplicacion/', views.multiplicacion_view, name='multiplicacion'),
    path('division/', views.division_view, name='division'),
]
