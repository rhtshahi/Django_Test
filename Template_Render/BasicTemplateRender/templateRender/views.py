from multiprocessing import context
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(pages):
    # return HttpResponse('HOME')
    #-----use of variable-----#
    context={'variable':'This is sent from view!!!'}
    return render(pages, 'index.html', context)

def about(pages):
    # return HttpResponse('About')
    return render(pages, 'about.html')

def services(pages):
    # return HttpResponse('Services')
    return render(pages, 'services.html')

def contact(pages):
    # return HttpResponse('Contact')
    return render(pages, 'contact.html')