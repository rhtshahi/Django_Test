from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from app1.models import Contact
from django.contrib.messages import constants as messages
# from django.contrib.messages import messages

# Create your views here.
def index(request):
    context = {
        'variable': 'This is sent from view.py'
    }
    # return HttpResponse('This is Home Page.')
    # messages.success(request, 'This is a test message.')
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse('This is About Page.')
    return render(request, 'about.html')

def services(request):
    # return HttpResponse('This is Services Page.')
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse('This is Contact Page.')
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        # messages.success(request, 'Message Sent!!!.')
    return render(request, 'contact.html')