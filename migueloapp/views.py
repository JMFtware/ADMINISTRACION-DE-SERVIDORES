from django.shortcuts import render

# Create your views here.

# Controlador de la vista de quienes somos
def quienesSomos(request):
    return render(request, 'quienesSomos.html')


# Controlador de los sectores
def sectoresEspecializacion(request):
    return render (request, 'sectoresEspecializacion.html')

    # Controlador de la pagina principal
def principal (request):

    return render(request, 'principal.html')


# Controlador de la vista del plan del marketing
def plan_marquetin(request):
    return render(request, 'plan_marquetin.html')

# Constrolador de los servicios que ofrecemos

def servicios (request):
    return render(request, 'servicios.html')