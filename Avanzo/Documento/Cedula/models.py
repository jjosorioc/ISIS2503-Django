from django.db import models
from Documento.models import Documento


class Cedula(Documento):

    nombres = models.CharField(max_length=50)

    apellidos = models.CharField(max_length=50)

    # Número de cédula
    numero = models.CharField(max_length=50)

    fechaNacimiento = models.DateField()

    lugarNacimiento = models.CharField(max_length=50)

    sexo = models.CharField(max_length=1)
