from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'menus/index.html')
        else:
            messages.info(request, 'Username or Password incorrect')
    elif request.user.is_authenticated:
        return render(request, 'menus/index.html')
    else:
        return render(request, 'menus/login.html')

