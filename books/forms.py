from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author_name',
            'description',
            'url',
            # 'created_at',
        ]
