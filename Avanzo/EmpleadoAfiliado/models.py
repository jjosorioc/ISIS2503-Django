from django.db import models
from EmpresaAfiliada.models import EmpresaAfiliada


class EmpleadoAfiliado(models.Model):
    # Nombre del afiliado
    nombre = models.CharField(max_length=50)

    #Identificación del afiliado
    identificacion = models.CharField(max_length=15)

    # Una empresa tiene varios empleados
    empresa = models.ForeignKey(EmpresaAfiliada, on_delete=models.CASCADE)
    