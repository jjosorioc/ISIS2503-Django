from django.shortcuts import render


from .logic.logic_asesorAvanzo import  get_solicitudes, getSolicitudesByEmpleado




def listaSolicitudes(request):
    solicitudes = get_solicitudes()
    
    id=request.GET.get('q')
    if id != None:

        print("id " ,id)
        old = solicitudes
        solicitudes = getSolicitudesByEmpleado(id)

        if (solicitudes == None):
            solicitudes = old
    
    return render(request, 'asesor.html', {'solicitudes': solicitudes})