from django.shortcuts import render, redirect
from .forms import BookForm

from books.models import Book

# Create your views here.


def list_books(request):
    book = Book.objects.all().order_by("title")
    return render(request, "books/list_books.html", {"book": book})


def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')
    return render(request, "books/add_book.html", {"form": form})
