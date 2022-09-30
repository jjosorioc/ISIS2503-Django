from django.db import models
from Solicitud.models import Solicitud


class Documento(models.Model):
    """Súper Clase de Documentos

    Args:
        models (tipo): Tipo de documento
        models (solicitud): La solicitud que contiene al documento
    """
    
    class Enumeracion(models.TextChoices):
        """Representa el tipo de documento.

        Args:
            models (tipo): Nombre Completo
        """
        COMPROBANTE_PAGO= ("CP", "Comprobante de Pago")
        CERTIFICACION_BANCARIA = ("CB", "Certificación Bancaria")
        CEDULA = ("CE", "Cédula")
        CERTIFICACION_LABORAL = ("CL", "Certificación Laboral")


    tipo = models.CharField(
        max_length = 2,
        choices = Enumeracion.choices,
    )


    solicitud = models.ForeignKey(Solicitud, on_delete = models.CASCADE)
