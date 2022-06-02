from django.shortcuts import render
from travel.models import Categories, Travels


def travel(request):
    return render(request, 'travel.html')

def category_list(request):
    categories = Categories.objects.all()
    context = {'categories': categories}
    return render(request, 'category-list.html', context = context)

def travel_list(request):
    travels = Travels.objects.all()
    context = {'travels': travels}
    return render(request, 'travel-list.html', context = context)

def contact(request):
    return render(request, 'contact.html')
