from django.shortcuts import render
from django.http import HttpResponse
from books.models import Books, Authors, Editorials, Genres
from books.forms import Book_form


def books(request):
    return render(request, 'books.html')

def books_list(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'books-list.html', context = context)

def authors_list(request):
    authors = Authors.objects.all()
    context = {'authors': authors}
    return render(request, 'authors-list.html', context = context)

def editorials_list(request):
    editorials = Editorials.objects.all()
    context = {'editorials': editorials}
    return render(request, 'editorials-list.html', context = context)

def genres_list(request):
    genres = Genres.objects.all()
    context = {'genres': genres}
    return render(request, 'genres-list.html', context = context)

"""
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
        
"""

def contact(request):
    return render(request, 'contact.html')
