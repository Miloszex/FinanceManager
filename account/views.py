from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return render(request, 'account/signup_success.html')
        else:
            form = LoginForm()
    return render(request, 'account/signup.html', {'form': form})


def signin(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return render(request, 'account/signin_success.html')
            else:
                pass
        else:
            form = LoginForm()
    return render(request, 'account/signin.html', {'form': form})


def signout(request):
    logout(request)
    return render(request, 'account/signout.html', {'message': 'You have been logged out successfully!'})
