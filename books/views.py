from django.shortcuts import render, redirect
from .forms import BookForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from books.models import Book, User

#### ------------------------------------------------------------------------
#### Registration stuff
#### https://pythonprogramming.net/user-registration-django-tutorial/
#### https://docs.djangoproject.com/en/3.2/topics/auth/default/
#### ------------------------------------------------------------------------
from .forms import SignupForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth import get_user_model
User = get_user_model()


def login_custom(request):
    user = authenticate(username='johann', password='tweedlemeister')
    if user is not None:
        login(request, user)
        return HttpResponse("Logged in!")
    else:
        return HttpResponse("Not logged in.")

def logout_custom(request):
    logout(request)
    return HttpResponse("Logged out!")
#    return redirect("")

def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("/")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})
    else:
        form = SignupForm
        return render(request = request,
                      template_name = "register.html",
                      context={"form":form})
# Create your views here.
#### ------------------------------------------------------------------------


def list_books(request):
    books = Book.objects.all().order_by("title")
    if (request.user.id != None):
        user = User.objects.get(id=request.user.id)
        favorites = user.favorite_books.all()
    else:
        favorites = []
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
