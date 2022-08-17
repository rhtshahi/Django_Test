from django.shortcuts import render, HttpResponse

# Create your views here.
def home(page):
    # return HttpResponse('This is home page')
    return render(page, 'index.html')

def about(page):
    # return HttpResponse('This is home page')
    return render(page, 'about.html')

def bookList(page):
    # return HttpResponse('Books')
    return render(page, 'books.html')

def author(page):
    # return HttpResponse('Author Page')
    return render(page, 'author.html')