from django.db import models
from Solicitud.models import Solicitud
from EmpresaAfiliada.models import EmpresaAfiliada

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


    solicitud = models.ForeignKey(Solicitud, on_delete = models.CASCADE, null = True)
    
    class Meta:
        abstract = True



class CertificacionLaboral(Documento):
    """
    Certificación Laboral
    """
    
    # Nombre del afiliado
    nombre = models.CharField(max_length=50)

    #Identificación del afiliado
    numCedula = models.CharField(max_length=15)

    empresa = models.ForeignKey(EmpresaAfiliada, on_delete=models.CASCADE)
    
    lugarExpedicion = models.CharField(max_length=100)

    salario = models.FloatField()

    terminoContrato = models.CharField(max_length=100) 

    def __str__(self) -> str:
        return str(self.nombre) + " | " + str(self.empresa) + " | "+ self.terminoContrato



class Cedula(Documento):
    """
    Cédula
    """

    nombres = models.CharField(max_length=50)

    apellidos = models.CharField(max_length=50)

    # Número de cédula
    numero = models.CharField(max_length=50)

    fechaNacimiento = models.DateField()

    lugarNacimiento = models.CharField(max_length=50)

    sexo = models.CharField(max_length=1)

    def __str__(self) -> str:
        return self.nombres + " " + self.apellidos + " | " + self.numero



class CertificacionBancaria(Documento):
    """Certificación Bancaria

    """

    # Documento de identificación de la persona
    tipoDocumento = models.CharField(max_length=30)

    # Número del documento
    numDocumento = models.CharField(max_length=15)


    medioEnvio = models.CharField(max_length=30)

    # Correo de la persona
    correo = models.CharField(max_length=30)


    # Quien quiere ver la certificación bancaria
    destinatario = models.CharField(max_length=50)

    bancoCuenta = models.CharField(max_length=50)

    tipoCuenta = models.CharField(max_length=30)

    numeroCuenta = models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.destinatario) + " | "+ self.bancoCuenta + " | " + self.tipoCuenta + " | " + self.numeroCuenta


class ComprobantePago(Documento):

    empresaComprobante = models.ForeignKey(EmpresaAfiliada, on_delete=models.CASCADE)

    idComprobante = models.CharField(max_length=50)

    destinatario = models.CharField(max_length=50)

    cantidad = models.FloatField()

    ciudad = models.CharField(max_length = 50)

    fecha = models.DateField()

    direccion = models.CharField(max_length = 50)


    def __str__(self) -> str:
        return str(self.empresaComprobante) + " | "+ self.destinatario + " | " + str(self.cantidad) 