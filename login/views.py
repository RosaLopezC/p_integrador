from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario  # Asegúrate de tener un modelo llamado Usuario
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_view(request):
    return render(request, 'login/login.html')


def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST['name']
        fecha_nacimiento = request.POST['birthdate']
        correo = request.POST['email']
        contrasena = request.POST['password']

        # Verificar si ya existe un usuario con el mismo correo
        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo ya está registrado. Por favor, elige otro o inicia sesión.')
            return redirect('registro')

        # Cálculo de la edad
        fecha_nac = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
        hoy = datetime.date.today()
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))

        # Determinar el tipo de cuenta según la edad
        if edad < 18:
            tipo_cuenta = 'estudiante'
        else:
            tipo_cuenta = request.POST.get('accountType', 'normal')

        # Guardar el usuario en la base de datos
        usuario = Usuario(nombre=nombre, fecha_nacimiento=fecha_nac, correo=correo, contrasena=contrasena, tipo_cuenta=tipo_cuenta)
        usuario.save()

        messages.success(request, 'Usuario registrado con éxito')
        return redirect('iniciar_sesion')

    return render(request, 'login/registro.html')


def iniciar_sesion(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # Intentar autenticación con el correo o el nombre de usuario
        user = authenticate(request, username=username_or_email, password=password)
        
        if user is not None:
            login(request, user)  # Iniciar sesión
            return redirect('menu')  # Redirigir al menú si el usuario es autenticado correctamente
        else:
            messages.error(request, 'Credenciales incorrectas, intenta nuevamente.')
            return redirect('iniciar_sesion')

    return render(request, 'login/iniciar_sesion.html')


def menu(request):
    return render(request, 'menu/menu.html')

def numeros_view(request):
    return render(request, 'primaria/numeros.html')

def sumas_restas_view(request):
    return render(request, 'primaria/sumas_restas.html')

def secuencias_view(request):
    return render(request, 'primaria/secuencias.html')

def geometria_view(request):
    return render(request, 'primaria/geometria.html')

def medidas_view(request):
    return render(request, 'primaria/medidas.html')

def fracciones_view(request):
    return render(request, 'primaria/fracciones.html')

def multiplicacion_view(request):
    return render(request, 'primaria/multiplicacion.html')

def division_view(request):
    return render(request, 'primaria/division.html')
