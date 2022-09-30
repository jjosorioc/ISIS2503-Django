from django.shortcuts import render
from logic.logic_empleadoAfiliado import get_solicitudesByEmpleado, get_empleado_by_identificacion



def solicitudByEmpleado(request, empleado: str):
    objetoEmpleado = get_empleado_by_identificacion(empleado)
    solicitudes = get_solicitudesByEmpleado(objetoEmpleado)

    return render(request, 'asesor.html', {'solicitudes': solicitudes})
    