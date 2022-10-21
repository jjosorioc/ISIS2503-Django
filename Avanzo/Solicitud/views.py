from django.shortcuts import render

from Documento.models import CertificacionLaboral
from Documento.models import ComprobantePago
from Documento.models import CertificacionBancaria
from Documento.models import Cedula
from Solicitud.logic.logic_solicitud import getSolicitudesByEmpleado
from Solicitud.models import Solicitud
from django.core.files.storage import FileSystemStorage
from Solicitud.logic.logic_solicitud import get_solicitudes
from EmpresaAfiliada.models import EmpresaAfiliada
import pytesseract
from pdf2image import convert_from_path

def listaSolicitudes(request):
    solicitudes=get_solicitudes()

    id=request.GET.get('q')
    if id != None:
        old=solicitudes
        solicitudes=getSolicitudesByEmpleado(id)

        if(solicitudes==None):
            solicitudes=old
    return render(request, 'solicitud.html', {'solicitudes': solicitudes})

def getSolicitudById(id):
    queryset=Solicitud.objects.get(id=id)
    return queryset


def detailSolicitud(request, id):
    """_summary_

    Args:
        request (_type_): _description_
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    solicitud = getSolicitudById(id)
    if request.method=="POST":
        uploaded_file=request.FILES['file']
        tipo=request.POST.get('tipo')
        fs=FileSystemStorage()
        nombre="documentos/"+str(solicitud.id) + "_" + tipo + ".pdf"  # type: ignore
        fs.delete(nombre)
        name=fs.save(nombre, uploaded_file)

        mapeoSegunDocumento(fs.path(name), tipo, solicitud.id)  # type: ignore
        
        fs.delete(nombre)   
    return render(request, 'detailSolicitud.html', {'solicitud': solicitud})



def mapeoSegunDocumento(path: str, tipo: str, idSolicitud: int) -> bool:
    """Busca el tipo de documento y lo mapea a la base de datos

    Args:
        path (str): path a donde se guardó el documento
        tipo (str): Tipo de documento
        idSolicitud (int): ID de la solicitud

    Returns:
        bool: True si se agregó el documento, False si no
    """
    doc = convert_from_path(path, 500)

    if tipo == 'CP':
        return mapearComprobantePago(doc[0], idSolicitud)
    elif tipo == 'CB':
        return mapearCertificacionBancaria(doc[0], idSolicitud)
    elif tipo == 'CE':
        return mapearCedula(doc[0], idSolicitud)
    elif tipo == 'CL':
        return mapearCertificacionLaboral(doc[0], idSolicitud)
        
    return False


def mapearComprobantePago(doc, idSolicitud: int):
    text = pytesseract.image_to_string(doc, lang='eng+spa')
    listaSegunLineas = text.split('\n')
    atributos = {
        'tipo': 'CP',
        'solicitud': Solicitud.objects.get(id=idSolicitud),
        'empresaComprobante': None, # FK de EmpresaAfiliada
        'idComprobante': None,
        'destinatario': None,
        'cantidad': None,
        'ciudad': None,
        'fecha': None,
        'direccion': None
        
    }

    for linea in listaSegunLineas:

        for i in ['empresa', 'compañía', 'empresa afiliada']:
            if i in linea.lower():
                nombreObtenido = linea.split(': ')[1].replace('  ', ' ')
                try:
                    objectEmpresa = EmpresaAfiliada.objects.get(nombre=nombreObtenido)
                    atributos['empresaComprobante'] = objectEmpresa
                except:
                    atributos['empresaComprobante'] = None
        for i in ['comprobante', 'número', 'numero']:
            if i in linea.lower():
                atributos['idComprobante'] = linea.split(': ')[1].replace('  ', ' ') 
        for i in ['destinatario', 'beneficiario', 'cliente']:
            if i in linea.lower():
                atributos['destinatario'] = linea.split(': ')[1].replace('  ', ' ')
        for i in ['cantidad', 'valor', 'valor total']:
            if i in linea.lower():
                num = linea.split(': ')[1].strip(" $.")
                num = num.replace('.','')
                atributos['cantidad'] = float(num.replace(',','.'))
        for i in ['ciudad', 'ciudad de']:
            if i in linea.lower():
                atributos['ciudad'] = linea.split(': ')[1].replace('  ', ' ')
        for i in ['fecha', 'fecha de']:
            if i in linea.lower():
                # Año-Mes-Día
                fechaString = linea.split(': ')[1].replace('  ', ' ').replace('/', '-')
                
                atributos['fecha'] =  fechaString
        for i in ['dirección', 'direccion', 'lugar']:
            if i in linea.lower():
                atributos['direccion'] = linea.split(': ')[1].replace('  ', ' ')

    for key in atributos:
        if atributos[key] == None:
            return False

    ComprobantePago.objects.create(
        tipo = atributos['tipo'],
        solicitud = atributos['solicitud'],
        empresaComprobante = atributos['empresaComprobante'],
        idComprobante = atributos['idComprobante'],
        destinatario = atributos['destinatario'],
        cantidad = atributos['cantidad'],
        ciudad = atributos['ciudad'],
        fecha = atributos['fecha'],
        direccion = atributos['direccion']
    )
    
                
    return True

def mapearCertificacionBancaria(doc, idSolicitud: int):
    text = pytesseract.image_to_string(doc, lang='eng+spa')
    listaSegunLineas = text.split('\n')
    atributos = {
        'tipo': 'CB',
        'solicitud': Solicitud.objects.get(id=idSolicitud),
        'tipoDocumento': None,
        'numDocumento': None,
        'medioEnvio': None,
        'correo': None,
        'destinatario': None,
        'bancoCuenta': None,
        'tipoCuenta': None,
        'numeroCuenta': None,
    }

    for linea in listaSegunLineas:

        for i in ['tipo de documento', 'tipo documento']:
            if i in linea.lower():
                atributos['tipoDocumento'] = linea.split(': ')[1].replace('  ', ' ')
        for i in ['número de documento', 'numero de documento']:
            if i in linea.lower():
                atributos['numDocumento'] = linea.split(': ')[1].replace('  ', ' ')
        for i in ['medio de envío', 'medio envio', 'envío', 'envio', "medio de envio"]:
            if i in linea.lower():
                atributos['medioEnvio'] = linea.split(': ')[1].replace('  ', ' ')
        for i in ['correo', 'e-mail', 'email']:
            if i in linea.lower():
                atributos['correo'] = linea.split(': ')[1].replace('  ', ' ').replace('(W', '@')
        for i in ['destinatario', 'beneficiario', 'cliente']:
            if i in linea.lower():
                atributos['destinatario'] = linea.split(': ')[1].replace('  ', ' ')
        for i in ['banco', 'banco de']:
            if i in linea.lower():
                atributos['bancoCuenta'] = linea.split(': ')[1].replace('  ', ' ')
        for i in ['tipo de cuenta', 'tipo cuenta']:
            if i in linea.lower():
                atributos['tipoCuenta'] = linea.split(': ')[1].replace('  ', ' ')
        for i in ['número de cuenta', 'numero de cuenta']:
            if i in linea.lower():
                atributos['numeroCuenta'] = linea.split(': ')[1].replace('  ', ' ')

    print(atributos)
    for key in atributos:
        if atributos[key] == None:
            return False

    CertificacionBancaria.objects.create(
        tipo = atributos['tipo'],
        solicitud = atributos['solicitud'],
        tipoDocumento = atributos['tipoDocumento'],
        numDocumento = atributos['numDocumento'],
        medioEnvio = atributos['medioEnvio'],
        correo = atributos['correo'],
        destinatario = atributos['destinatario'],
        bancoCuenta = atributos['bancoCuenta'],
        tipoCuenta = atributos['tipoCuenta'],
        numeroCuenta = atributos['numeroCuenta']
    )
    
    return True

def mapearCedula(doc, idSolicitud: int):
    text = pytesseract.image_to_string(doc, lang='eng+spa')
    print(text)
    return True

def mapearCertificacionLaboral(doc, idSolicitud: int):
    """Mapea la certificación laboral a la base de datos

    Args:
        doc (_type_): _description_
        idSolicitud (int): _description_

    Returns:
        _type_: _description_
    """
    text = pytesseract.image_to_string(doc, lang='eng+spa')
    listaSegunLineas = text.split('\n')
    atributos = {
        'tipo': 'CL',
        'nombre': None,
        'numCedula': None,
        'empresa': None,
        'lugarExpedicion': None,
        'salario': None,
        'terminoContrato': None,
        'solicitud': Solicitud.objects.get(id=idSolicitud)
    }

    for linea in listaSegunLineas:

        for i in ['nombre', 'nombres']: 
            if i in linea.lower():
                atributos['nombre'] = linea.split(': ')[1].replace('  ', ' ')

        for i in ['cédula', 'cédula de ciudadanía', 'cc', 'cedula', 'identificación', "identificacion"]:
            if i in linea.lower():
                atributos['numCedula'] = int(linea.split(': ')[1].replace(' ', ''))

        for i in ['empresa', 'empresa donde labora', 'afiliada']:
            if i in linea.lower():
                nombreObtenido = linea.split(': ')[1].replace('  ', ' ')
                try:
                    
                    objectEmpresa = EmpresaAfiliada.objects.get(nombre=nombreObtenido)
                
                    atributos['empresa'] = objectEmpresa
                except Exception as e:
                    atributos['empresa'] = None

        for i in ['lugar de expedición', 'lugar de expedicion', 'lugar de expedicion de la cedula', 'lugar de expedicion de la cédula', 'nacimiento']: 
            if i in linea.lower():
                atributos['lugarExpedicion'] = linea.split(': ')[1].replace('  ', ' ')
        for i in ['salario', 'salario mensual', 'salario mensual devengado']:
            if i in linea.lower():
                num = linea.split(': ')[1].strip(" $.")
                num = num.replace('.','')
                atributos['salario'] = float(num.replace(',','.'))

        for i in ['termino del contrato', 'termino del contrato de trabajo', 'termino del contrato de trabajo o fecha de retiro', 'contrato']:
            if i in linea.lower():
                atributos['terminoContrato'] = linea.split(': ')[1].replace('  ', ' ')

    for key in atributos:
        if atributos[key] == None:
            return False
    CertificacionLaboral.objects.create(
        tipo=atributos['tipo'],
        solicitud=atributos['solicitud'],
        nombre = atributos['nombre'],
        numCedula = atributos['numCedula'],
        empresa = atributos['empresa'],
        lugarExpedicion = atributos['lugarExpedicion'],
        salario = atributos['salario'],
        terminoContrato = atributos['terminoContrato']
    )
    return True