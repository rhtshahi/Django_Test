from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def registerPage(request):
    # return render(request, 'register.html')
    if request.user.is_authenticated:
        return redirect('home')

    else:

        form = CreateUserForm()

        if request.method=='POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user_name = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user_name )
                return redirect('login')

        context={'form':form}
        return render(request, 'register.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    else:

        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username, password)

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')#redirect is not for html file but for name of url or path

            else:
                messages.info(request, 'Incorrect Username/Password!!!')
                return render(request, 'login.html')

        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def userPage(request):
    return render(request, 'user.html')