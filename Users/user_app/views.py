import cmath
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate, user_logged_in
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def base(request):
    return render(request,'user_app/base.html')


def home(request):
    return render(request,'user_app/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            login(request,user)
            messages.success(request,"you are in ")
            return redirect('home')
        else:
            messages.error(request,"try again !")
            return redirect('register')
    
    form = UserRegisterForm
    return render(request, 'user_app/register.html',{'form':form})



def login_req(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if  form.is_valid():
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You don't have a {username}.?")
                return redirect('home')
            else:
                messages.error(request,"wop!!! Sorry")
        else:
            messages.error(request,"invaild totely") 
    form = AuthenticationForm()               
    
    return render (request, 'user_app/login.html',{'login_form':form})


def logout_req(request):
    logout(request)
    messages.info(request,"you are out of the web see you soon.")
    return redirect('home')