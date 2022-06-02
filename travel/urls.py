from django.urls import path
from travel.views import travel, category_list, travel_list, travel_create, contact

urlpatterns =[
    path('', travel, name = 'travel'),
    path('listar-categorias/', category_list, name = 'category_list'),
    path('listar-viajes/', travel_list, name = 'travel_list'),
    path('crear-viaje/', travel_create, name = 'travel_create'),
    path('contacto/', contact, name = 'contact')
]
