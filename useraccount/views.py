from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {})


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "User Successfully created!!")

            return redirect('login')

    context = {'form': form}
    return render(request, 'user/registration.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")

    return render(request, 'user/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')
