from django.db import models


class AsesorAvanzo(models.Model):
    nombre = models.CharField(max_length=50)

    identificacion = models.CharField(max_length=15)

    def __str__(self) -> str:
        return str(self.nombre)