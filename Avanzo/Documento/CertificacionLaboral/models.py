from django.db import models
from Documento.models import Documento


class CertificacionLaboral(Documento):
    
    # Nombre del afiliado
    nombre = models.CharField(max_length=50)

    #Identificación del afiliado
    numCedula = models.CharField(max_length=15)

    lugarExpedicion = models.CharField(max_length=100)

    salario = models.FloatField()

    terminoContrato = models.CharField(max_length=100)    
