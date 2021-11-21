from django.db import models
from django.urls import reverse

class News(models.Model):
    # Поле первичного ключа делается автоматически

    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')  # blank=True - не обязательное к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    # есть ещё FileField и то и другое загружает путь к файлу
    # upload_to - куда сохранять | filefield - любой файл, imagefield - проверяет на картинки
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')  # если не указать значение по умолчанию то будет None
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'  # название в единсвенном
        verbose_name_plural = 'новости'  # название в множественном
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категорий')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'  # название в единсвенном
        verbose_name_plural = 'Категории'  # название в множественном
        ordering = ['title']


# после создания бд нужно сделать миграцию, они необходимы для того что бы делать связи, делается самостоятельно по
# модели
# создаются с помощью make migration
