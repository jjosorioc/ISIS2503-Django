from Solicitud.models import Solicitud
from EmpleadoAfiliado.models import EmpleadoAfiliado

from AsesorAvanzo.models import AsesorAvanzo



def get_empleadosAfiliados():
    queryset = EmpleadoAfiliado.objects.all()

    return queryset

def getSolicitudesByEmpleado(id):
    empleados = get_empleadosAfiliados()
    try:
        
        empleados = empleados.get(identificacion=id)
    
        queryset = Solicitud.objects.filter(empleadoAfiliado = empleados)
        print("By Empleado: " , queryset)
        return queryset
    except:
        return None


def get_solicitudes():
    queryset = Solicitud.objects.all()

    return queryset