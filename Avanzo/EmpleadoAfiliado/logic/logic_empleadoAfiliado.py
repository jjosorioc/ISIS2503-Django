
from Avanzo.Solicitud.models import Solicitud
from EmpleadoAfiliado.models import EmpleadoAfiliado

def get_empleados():
    queryset = EmpleadoAfiliado.objects.all()
    return queryset


def get_solicitudes():
    queryset = Solicitud.objects.all()
    return queryset


def get_solicitudesByEmpleado(empleado):
    queryset = Solicitud.objects.filter(empleadoAfiliado=empleado)

    return queryset


def get_empleado_by_identificacion(id: str):

    query = EmpleadoAfiliado.objects.get(identificacion=id)
    return query