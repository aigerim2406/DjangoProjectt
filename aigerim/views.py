from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


menu = ["О нас", "Добавить", "Обратная связь", "Войти"]
def index(request): #HttpRequest
    posts = Aigerim.objects.all()
    return render(request, 'aigerim/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request): #HttpRequest
    return render(request, 'aigerim/about.html', {'menu': menu, 'title': 'О нас'})

def categories(request):
    return HttpResponse("<h1>aceccories по категориям</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')