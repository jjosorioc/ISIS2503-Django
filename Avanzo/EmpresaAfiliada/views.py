from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Avanzo.auth0backend import getRole
from EmpresaAfiliada.logic.logic_EmpresaAfiliada import get_empresasAfiliadas
from django.core.files.storage import FileSystemStorage
from EmpresaAfiliada.models import EmpresaAfiliada
import pytesseract
from django.http import HttpResponse
from pdf2image import convert_from_path

@login_required
def listaEmpresas(request):
    role=getRole(request)
    if role =="Empresa Afiliada":
        empresas=get_empresasAfiliadas()

        return render(request, 'empresa.html', {'empresas': empresas})
    else:
        return HttpResponse("Unauthorized User")


# Create your views here.
