from django.shortcuts import render


from .logic.logic_asesorAvanzo import  get_solicitudes, getSolicitudesByEmpleado


def listaSolicitudPorEmpleado(request):
    
    

    return render(request, 'asesor.html', {'solicitudesFilter': solicitudes})

def listaSolicitudes(request):
    solicitudes = get_solicitudes()
    
    id=request.GET.get('q')
    print("id " ,id)
    solicitudes = getSolicitudesByEmpleado(id)
    
    return render(request, 'asesor.html', {'solicitudes': solicitudes})