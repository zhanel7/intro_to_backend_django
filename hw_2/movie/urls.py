from django.urls import path
from .views import movie_list, movie_detail, movie_list_page

urlpatterns = [
    path('', movie_list, name='movie-list'),  # Список фильмов
    path('<int:id>/', movie_detail, name='movie-detail'),  # Детальная информация о фильме
    path('page/', movie_list_page, name='movie-list-page'),  # HTML-страница со списком фильмов
]
