from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# Create your views here.

def base(request):
    return render(request,'user_app/base.html')


def home(request):
    return render(request,'user_app/home.html')


def register(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("you been registered")
            return redirect('home')
        else:
            print("it is not registered try again")
            return redirect('register')
    
    return render(request, 'user_app/register.html',{'form':form})

def login(request):
    return render (request, 'user_app/login.html')
