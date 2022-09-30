
from empleado.models import Empleado

def get_empleados():
    queryset = Empleado.objects.all()
    return queryset

