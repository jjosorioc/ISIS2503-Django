from email.policy import default
from random import choices
from django.db import models
from EmpleadoAfiliado.models import EmpleadoAfiliado

class Solicitud(models.Model):

    # One to Many
    empleadoAfiliado = models.ForeignKey(EmpleadoAfiliado, on_delete=models.CASCADE)

    cantidad = models.FloatField()

    fechaPago = models.DateField()  

    class Enumeracion(models.TextChoices):
        """Clase que representa la enumeración del estado de una solicitud

        Args:
            models (Estado): Nombre Completo
        """
        APROBADO = ('AP', 'Aprobado')
        REPROBADO = ('RP', 'Reprobado')
        REINTENTE = ('RE', 'Reintente subiendo documentos más fiables')

    estado = models.CharField(
        max_length = 2,
        choices = Enumeracion.choices,
        default = Enumeracion.REPROBADO
    )

    
        