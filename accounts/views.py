from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'accounts/home.html')

def signup_view(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html',{'form': form})

def signin_view(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html',{'form': form})

def logout_view(request):
    logout(request)
    return redirect('signin')

def user_list(request): 
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request,'accounts/user_list.html',{'users':users})
    else:
        return redirect('home')