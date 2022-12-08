from django.urls import path
from . import views

urlpatterns = [
    path('empresas/', views.listaEmpresas, name="listaEmpresas"),
]
