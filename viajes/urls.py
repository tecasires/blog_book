from django.urls import path
from viajes.views import listar_viajes, listar_categorias, contacto, viajes

urlpatterns =[
    path('', viajes, name = 'viajes'),
    path('listar_viajes/', listar_viajes, name = 'listar_viajes'),
    path('listar_categorias/', listar_categorias, name = 'listar_categorias'),
    path('contacto/', contacto, name = 'contacto')
]
