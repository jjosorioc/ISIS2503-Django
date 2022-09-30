from django.db import models


class EmpresaAfiliada(models.Model):

    nombre = models.CharField(max_length=50)