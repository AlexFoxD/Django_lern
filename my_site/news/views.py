from django.shortcuts import render
from django.http import HttpResponse

from .models import News

# часть приложения которая обрабатывает запрос

# request обязательный параметр который передаётся в функцию
# для того что бы было видно нужно идти в маршрутизатор (urls.py)

def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})

