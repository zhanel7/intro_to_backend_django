from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('articles/', article_list),
    path('articles/<int:id>/', article_detail),
]