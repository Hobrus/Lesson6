from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, BaseUserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect('hello')
                # Перенаправление на главную страницу
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def hello(request):
    return HttpResponse("Hello world!")


def user_registration(request):
    if request.method == "POST":
        form = BaseUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = BaseUserCreationForm()
    return render(request, 'registration.html', {'form': form})