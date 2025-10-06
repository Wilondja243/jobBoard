from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import UserForm, LoginForm

def signupView(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                role=form.cleaned_data['role']
            )

            if user.role.lower() == 'employer':
                return redirect('dashboard')
            elif user.role.lower() == 'candidate':
                return redirect('home')
            else:
                return redirect('home')
    else:
        form = UserForm()
    return render(request, 'authentification/signup.html', {'form': form})


def login_view(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if user.role == "employer":
                    return redirect('dashboard')
                elif user.role == 'candidate':
                    return redirect('home')
                else:
                    return redirect('home')
            else:
                message = "Identifiant incorrects."
    else:
        form = LoginForm()

    return render(request, 'authentification/login.html', {'form': form, 'message': message})


def logoutView(request):
    logout(request)
    return redirect('login')