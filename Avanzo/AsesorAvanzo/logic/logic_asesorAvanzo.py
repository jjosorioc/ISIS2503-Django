from Solicitud.models import Solicitud
from EmpleadoAfiliado.models import EmpleadoAfiliado

from AsesorAvanzo.models import AsesorAvanzo



def get_empleadosAfiliados():
    queryset = EmpleadoAfiliado.objects.all()

    return queryset

def getSolicitudesByEmpleado(id):
    queryset = Solicitud.objects.filter(empleadoAfiliado = id)
    print("By Empleado: " , queryset)
    return queryset


def get_solicitudes():
    queryset = Solicitud.objects.all()

    return queryset