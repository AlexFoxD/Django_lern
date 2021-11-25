from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from django.shortcuts import get_object_or_404, redirect, render
from .forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# часть приложения которая обрабатывает запрос

# request обязательный параметр который передаётся в функцию
# для того что бы было видно нужно идти в маршрутизатор (urls.py)

def test(request):
    objects = ['1', '2', '3', '4', '5', '6', '7', '8']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page',1)
    page_odj = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_odj})


class HomeNews(ListView):   # замена def index
    model = News
    context_object_name = 'news'
    template_name = 'news/index.html'
    sekextra_context = {'title': 'Главная'}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):    # фильтр объектов
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/index.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):    # фильтр объектов
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):     # Чтение персональной записи
    model = News
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):     # Создание формы
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # login_url = '/admin/'
    raise_exception = True
