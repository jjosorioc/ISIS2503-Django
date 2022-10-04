from django.shortcuts import render

from Solicitud.models import Solicitud


from .logic.logic_asesorAvanzo import  get_solicitudes, getSolicitudesByEmpleado




def listaSolicitudes(request):
    solicitudes = get_solicitudes()
    
    id=request.GET.get('q')
    if id != None:

        old = solicitudes
        solicitudes = getSolicitudesByEmpleado(id)

        if (solicitudes == None):
            solicitudes = old
    
    return render(request, 'asesor.html', {'solicitudes': solicitudes})

def getSolicitudById(id):
    queryset = Solicitud.objects.get(id=id)
    return queryset   

def detailSolicitud(request, id):
    print("id: ", id)
    solicitud = getSolicitudById(id)
    return render(request, 'detailSolicitud.html', {'solicitud': solicitud})