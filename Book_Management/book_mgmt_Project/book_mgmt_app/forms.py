from django import forms
# from django.forms import ModelForm
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        #fields = ['name', 'author', 'published_year']