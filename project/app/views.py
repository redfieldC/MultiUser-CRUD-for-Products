from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
import logging

logger = logging.getLogger()


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            user = CustomUser.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')

    return render(request, 'registration/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL you want to redirect to after login.
        else:
            logger.error(f'Failed login attempt for username: {username}')
            
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request,'registration/home.html')