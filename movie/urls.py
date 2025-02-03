
from django.urls import path
from .views import movie_list  # ✅ Здесь импортируем movie_list

urlpatterns = [
    path('movies/', movie_list, name='movie-list'),  # ✅ URL для списка фильмов
]