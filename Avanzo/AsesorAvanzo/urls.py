from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('asesor/', views.listaSolicitudes, name="listaSolicitudes"),
   
]