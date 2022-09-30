from email.policy import default
from random import choices
from django.db import models
from EmpleadoAfiliado.models import EmpleadoAfiliado
from AsesorAvanzo.models import AsesorAvanzo

class Solicitud(models.Model):

    # One to Many
    empleadoAfiliado = models.ForeignKey(EmpleadoAfiliado, on_delete=models.CASCADE)

    cantidad = models.FloatField()

    fechaPago = models.DateField()  

    asesor = models.ForeignKey(AsesorAvanzo, on_delete=models.CASCADE, null = True, blank = True)
    

    class Enumeracion(models.TextChoices):
        """Clase que representa la enumeración del estado de una solicitud

        Args:
            models (Estado): Nombre Completo
        """
        EN_ESPERA = ("EE", "En Espera")
        APROBADO = ('AP', 'Aprobado')
        REPROBADO = ('RP', 'Reprobado')
        REINTENTE = ('RE', 'Reintente subiendo documentos más fiables')

    estado = models.CharField(
        max_length = 2,
        choices = Enumeracion.choices,
        default = Enumeracion.EN_ESPERA
    )

    def __str__(self) -> str:
        return self.empleadoAfiliado.nombre + " | " + self.estado + " | " + str(self.fechaPago)
        