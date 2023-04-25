# Создание URL-маршрутов
# Определим URL-маршруты для нашего приложения

# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
# ]

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
