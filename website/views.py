from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request): 
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, message="Welcome to system")
            return redirect('home')
        else:
            messages.success(request, message="error detected")
            return redirect('home')
    return render(request, 'home.html')

def login_user(request):
    pass

def logout_user(request):
    pass