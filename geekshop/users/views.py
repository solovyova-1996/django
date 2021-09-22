from django.shortcuts import render
from .forms import UserLoginForm


def login(request):
    form = UserLoginForm()
    context = {
        'title': 'Geekshop - Авторизация',
        'form':form
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'Geekshop - Регистрация'
    }
    return render(request, 'users/register.html', context)
