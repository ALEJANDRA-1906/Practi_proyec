from django.db import models

# Create your models here
class Persona(models.Model):
    nombre = models.CharField(max_length=50) #Para campos ccn textos
    apellido = models.CharField(max_length=10)
    cedula = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(max_length=100)
    edad = models.IntegerField(default=18)