from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    tipo_cuenta = models.CharField(max_length=20)  # estudiante, padre, apoderado o normal

    def __str__(self):
        return self.nombre
