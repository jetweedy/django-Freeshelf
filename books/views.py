from django.shortcuts import render, redirect
from .forms import BookForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from books.models import Book, User

# Create your views here.


def list_books(request):
    books = Book.objects.all().order_by("title")
    user = User.objects.get(id=request.user.id)
    favorites = user.favorite_books.all()
    return render(request, "books/list_books.html", {"book": books, "favorites":favorites})

def favorite_books(request):
    if (request.user.id != None):
        user = User.objects.get(id=request.user.id)
        books = user.favorite_books.all()
        return render(request, "books/favorite_books.html", {"user":user, "books":books})
    else:
        return redirect(to='')

def add_favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.user.id)
    user.favorite_books.add(book)
    return redirect(to='list_books')

def remove_favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.user.id)
    user.favorite_books.remove(book)
    return redirect(to='list_books')

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')
    return render(request, "books/add_book.html", {"form": form})
