from django.urls import path
from books.views import books, books_list, authors_list, editorials_list, genres_list, contact


urlpatterns =[
    path('', books, name = 'book'),
    path('listar-libros/', books_list, name = 'book_list'),
    path('listar-autores/', authors_list , name = 'author_list'),
    path('listar_editoriales', editorials_list, name = 'editorials_list'),
    path('listar-generos/', genres_list, name = 'genres_list'),
    path('contacto/', contact, name = 'contact')
]
