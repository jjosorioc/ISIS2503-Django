
from Solicitud.models import Solicitud

def get_solicitudes():
    queryset = Solicitud.objects.all()
    return queryset
