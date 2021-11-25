import debug_toolbar
from django.conf import settings
from django.contrib import admin

from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='adminka'),
    # path('news/', include('news.urls')),  # подключение ссылок на другие страницы
    path('', include('news.urls')),         # (если будет передана'' то будет направленно сюда)
]

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # только для отладки для просмотра изображений
