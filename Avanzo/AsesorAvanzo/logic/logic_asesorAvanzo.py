from EmpleadoAfiliado.models import EmpleadoAfiliado

from AsesorAvanzo.models import AsesorAvanzo



def get_empleadosAfiliados():
    queryset = EmpleadoAfiliado.objects.all()

    return queryset