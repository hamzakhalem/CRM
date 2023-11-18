from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.

def home(request): 
    records = Record.objects.all()
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
    return render(request, 'home.html', {'records': records})

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

def customer_record(request, pk):
    if request.user.is_authenticated:
        # record = get_object_or_404(Record, id=pk)
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record': record})
    else:
        messages.success(request, message="Marakch login ya teti")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, message="Record deleted")
        return redirect('home')
    else:
        messages.success(request, message="Error deleting record")
        return redirect('home')