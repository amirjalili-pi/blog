from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "logged in successfully", "success")
                return redirect('blog:all_articles')
            else:
                messages.error(request, "your username or password is incorrect", "danger")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(request, 'your account have been created successfully', 'success')
            return redirect('accounts:user_login')

    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'you are successfully logged out', 'success')
    return redirect('blog:all_articles')

