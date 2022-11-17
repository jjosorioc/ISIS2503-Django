
from django.urls import path
from . import views

urlpatterns = [
    path('solicitudes/', views.listaSolicitudes, name="listaSolicitudes"),
    path('solicitudes/<int:id>', views.detailSolicitud, name="detailSolicitud"),
    path('solicitudes/<int:id>/edit', views.detailEditarSolicitud, name="detailEditar")
]