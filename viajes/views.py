from django.shortcuts import render
from viajes.models import Viajes, Categorias


# Create your views here.

def viajes(request):
        return render(request, 'viajes.html')

def listar_viajes(request):
        viajes = Viajes.objects.all()
        my_context = {'viajes':viajes}
        return render(request, 'listar_viajes.html', context=my_context)

def listar_categorias(request):
        viajes = Categorias.objects.all()
        my_context = {'viajes':viajes}
        return render(request, 'listar_categorias.html', context=my_context)

def contacto(request):
        return render(request, 'contacto.html')
