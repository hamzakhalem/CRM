from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
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

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, message="you logged out!")
    return redirect('/')

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password= password)
            login(request, user)
            messages.success(request, message="Welcome to system")
            return redirect('home')
        else:
            messages.success(request, message="error ya teti")
            return render(request, 'register.html', {'form': form})

    else:
        form = SignUpForm
        return render(request, 'register.html', {'form': form})
