from django import forms
from .models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title',
            'author_name',
            'description',
            'url',
            # 'created_at',
        ]
