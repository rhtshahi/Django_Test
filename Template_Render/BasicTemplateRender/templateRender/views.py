from django.shortcuts import render, HttpResponse

# Create your views here.
def home(pages):
    # return HttpResponse('HOME')
    return render(pages, 'index.html')

def about(pages):
    # return HttpResponse('About')
    return render(pages, 'about.html')

def services(pages):
    # return HttpResponse('Services')
    return render(pages, 'services.html')

def contact(pages):
    # return HttpResponse('Contact')
    return render(pages, 'contact.html')