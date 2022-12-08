
from Solicitud.models import Solicitud
from EmpleadoAfiliado.logic import logic_empleadoAfiliado as lea

def get_solicitudes():
    queryset = Solicitud.objects.all()
    return queryset

def getSolicitudesByEmpleado(id:str):
    empleados = lea.get_empleadosAfiliados()
    try:
        empleado = lea.get_empleado_by_identificacion(id)
        queryset = Solicitud.objects.filter(empleadoAfiliado = empleado)
        print("By Empleado: " , queryset)
        return queryset
    except:
        return None

