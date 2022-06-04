from django.shortcuts import render
from django.http import HttpResponse
from travel.models import Categories, Travels
from travel.forms import Travel_form


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

def travel_create(request):
    if request.method == 'GET':
        form = Travel_form
        context = {'form': form}
        return render(request, 'travel-create.html', context = context)
    else:
        form = Travel_form(request.POST)
        if form.is_valid():
            new_travel = Travels.objects.create(
                name = form.cleaned_data["name"],
                description = form.cleaned_data["description"],
                country =form.cleaned_data["country"],
                price = form.cleaned_data["price"],
                EAN = form.cleaned_data["EAN"],
                active = form.cleaned_data["active"]
            )
            context = {"new_travel": new_travel}
            return render(request, 'travel-create.html', context = context)
            
        #print(request.POST)
        return HttpResponse("Viniste por POST")
        

def contact(request):
    return render(request, 'contact.html')
