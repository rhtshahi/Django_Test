from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Book, Author
from .forms import BookForm

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
    context = {"book_list":queryset }
    return render(Book_page, 'books.html',context)


def author(Author_page):
    # return HttpResponse('Author Page')
    queryset = Author.objects.all()
    context = {'author_name':queryset}
    # return render(Author_page, 'author.html')
    return render(Author_page, 'author.html', context)

def bookCreate(create_book_page):
    form = BookForm()

    if create_book_page.method == 'POST':
        # print('Printing Post: ', create_book_page.POST)
        form = BookForm(create_book_page.POST)

        if form.is_valid():
            form.save()
            return redirect('/books')

    context ={'form': form}

    return render(create_book_page, 'book_create.html', context)

def bookUpdate(update_book_page, pk):

    book=Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if update_book_page.method == 'POST':
        # print('Printing Post: ', create_book_page.POST)
        form = BookForm(update_book_page.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('/books')
    
    context={'form': form}
    return render(update_book_page, 'book_update.html', context)

def AuthorDetails(author_details_page, pk):
    author_id=Author.objects.get(id=pk)
    # book_id=Book.objects.all()
    context={
        'author_id':author_id,
    }

    return render(author_details_page, 'author_details.html', context)