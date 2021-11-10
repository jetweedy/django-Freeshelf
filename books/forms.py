from django import forms
from .models import Book


#### ------------------------------------------------------------------------
#### Registration stuff
#### https://pythonprogramming.net/user-registration-django-tutorial/
#### ------------------------------------------------------------------------
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
#### ------------------------------------------------------------------------

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author_name',
            'description',
            'url',
        ]

