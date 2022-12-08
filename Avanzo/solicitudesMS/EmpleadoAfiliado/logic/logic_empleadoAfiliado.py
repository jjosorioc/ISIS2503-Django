
from Solicitud.models import Solicitud
from EmpleadoAfiliado.models import EmpleadoAfiliado

def get_empleadosAfiliados():
    queryset = EmpleadoAfiliado.objects.all()
    return queryset
def get_empleado_by_identificacion(id: str):

    query = EmpleadoAfiliado.objects.get(identificacion=id)
    return query