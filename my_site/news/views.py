from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category
from django.shortcuts import get_object_or_404, redirect
from .forms import NewsForm

# часть приложения которая обрабатывает запрос

# request обязательный параметр который передаётся в функцию
# для того что бы было видно нужно идти в маршрутизатор (urls.py)

def index(request):

    news = News.objects.all()
    context = {'news': news,
               'title': 'Список новостей'}

    return render(request, 'news/index.html', context=context)



def get_category(request, category_id):

    news = News.objects.filter(category_id=category_id)
    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)

    context = {'news': news,
               'category': category}

    return render(request, 'news/category.html', context=context)

def view_news(request, news_id):
    # news_item = News.objects.get(pk = news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/wiew_news.html', {"news_item": news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            page = News.objects.create(**form.cleaned_data)
            return redirect(page)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
