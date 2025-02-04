"""
URL configuration for hw_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views as movie_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', movie_views.movie_list),  # путь для фильмов
    path('movies/<int:id>/', movie_views.movie_list),  # путь для одного фильма
    path('articles/', blog_views.article_list),  # путь для статей
    path('articles/<int:id>/', blog_views.article_list),  # путь для одной статьи
]

from django.contrib import admin
from django.urls import path, include
from .views import home  # Импортируем представление

urlpatterns = [
    path('', home),  # Главная страница
    path('admin/', admin.site.urls),
    path('', include('movie.urls')),
    path('', include('blog.urls')),
]