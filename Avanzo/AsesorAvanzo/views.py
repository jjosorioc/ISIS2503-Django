from django.shortcuts import render


from .logic.logic_asesorAvanzo import get_empleadosAfiliados, get_solicitudes


def listaEmpleados(request):
    empleadosAfiliados = get_empleadosAfiliados()

    return render(request, 'asesor.html', {'empleadosAfiliados': empleadosAfiliados})

def listaSolicitudes(request):
    solicitudes = get_solicitudes()
    
    return render(request, 'asesor.html', {'solicitudes': solicitudes})