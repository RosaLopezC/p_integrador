from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    tipo_cuenta = models.CharField(max_length=20)  # estudiante, padre, apoderado o normal
    pfp = models.ImageField(upload_to="media/",null=True, blank=True)

    def __str__(self):
        return self.nombre

class Nivel_academico(models.Model):
    nombre = models.CharField(max_length=40)

class Grado (models.Model):
    nivel_academico = models.ForeignKey(Nivel_academico,models.PROTECT)
    nombre_grado = models.CharField(max_length=50)

class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    grado = models.ForeignKey(Grado,on_delete=models.PROTECT)

class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

class Dificultades(models.Model):
    nivel = models.CharField(max_length=20) #Facil, intermedio, dificil

class Leccion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length= 500)
    nivel_dificultad = models.ForeignKey(Dificultades,on_delete=models.PROTECT) #CAMBIAR
    tema = models.ForeignKey(Tema,on_delete=models.CASCADE)
    puntos_obtenidos = models.DecimalField(max_digits=4,decimal_places=2)
    orden = models.IntegerField()

class Pregunta(models.Model):
    enunciado = models.CharField(max_length=500)
    leccion = models.ForeignKey(Leccion,on_delete=models.CASCADE)

class Intento(models.Model):
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    respuesta_seleccionada = models.CharField(max_length=50)
    es_correcta = models.BooleanField()

