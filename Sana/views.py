from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login

def login_view(request):
    return render(request, 'accounts/login.html', {})

def home(request):
    return render(request, 'Sana/home.html', {})