from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Book, Author

# Create your views here.
def home(Home_page):
    # return HttpResponse('This is home page')
    return render(Home_page, 'index.html')

def about(About_page):
    # return HttpResponse('This is home page')
    return render(About_page, 'about.html')

def bookList(Book_page):
    # return HttpResponse('Books')
    queryset = Book.objects.all()
    context = {"book_list":queryset}
    return render(Book_page, 'books.html',context)


def author(Author_page):
    # return HttpResponse('Author Page')
    return render(Author_page, 'author.html')

