from django.shortcuts import render, HttpResponse

# Create your views here.
def home(pages):
    return HttpResponse('This is Home Page.')

def about(pages):
    return HttpResponse('This is About Page.')

def contact(pages):
    return HttpResponse('This is Contact Page.')

def services(pages):
    return HttpResponse('This is Services Page.')