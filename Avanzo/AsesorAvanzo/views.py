from django.shortcuts import render

from .logic.logic_asesorAvanzo import get_empleadosAfiliados


def listaEmpleados(request):
    empleadosAfiliados = get_empleadosAfiliados()

    return render(request, 'asesor.html', {'empleadosAfiliados': empleadosAfiliados})