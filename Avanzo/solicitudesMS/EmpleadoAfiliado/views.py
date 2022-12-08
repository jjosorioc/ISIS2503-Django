from django.shortcuts import render
from logic.logic_empleadoAfiliado import get_solicitudesByEmpleado, get_empleado_by_identificacion, get_solicitudes  # type: ignore


def solicitudes_list(request):
    solicitudes = get_solicitudes()
    return render(request, 'asesor.html', {'solicitudes': solicitudes})


def solicitudByEmpleado(request, empleado: str):
    objetoEmpleado = get_empleado_by_identificacion(empleado)
    solicitudes = get_solicitudesByEmpleado(objetoEmpleado)

    return render(request, 'asesor.html', {'solicitudes': solicitudes})
    