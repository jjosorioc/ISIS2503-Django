from django.db import models


class EmpresaAfiliada(models.Model):

    nombre = models.CharField(max_length=50)

    nit = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self) ->str:
        return str(self.nombre)