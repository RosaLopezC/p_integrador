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

        return HttpResponse("Usuario registrado con éxito")
    else:
        return render(request, 'login/registro.html')
    
def iniciar_sesion_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']

        # Autenticación por nombre de usuario o correo electrónico
        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirigir al dashboard después de iniciar sesión
        else:
            messages.error(request, 'Credenciales inválidas, por favor intenta de nuevo.')

    return render(request, 'login/iniciar_sesion.html')
