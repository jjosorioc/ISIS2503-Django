from EmpresaAfiliada.models import EmpresaAfiliada

def get_empresasAfiliadas():
    queryset = EmpresaAfiliada.objects.all()
    return queryset
