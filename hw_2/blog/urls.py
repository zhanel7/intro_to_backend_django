from django.urls import path
from .views import article_list, article_detail, article_list_page  # Импортируем новую вьюху

urlpatterns = [
    path('', article_list, name="article_list_api"),  # API (JSON)
    path('<int:id>/', article_detail, name="article_detail_api"),  # API (JSON)
    path('page/', article_list_page, name="article_list_page"),  # HTML-страница
]
