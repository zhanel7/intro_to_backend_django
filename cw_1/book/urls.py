from django.urls import path
from .views import book_list, book_detail

app_name = 'book'

urlpatterns = [
    path('books/page/', book_list, name='book-list-page'),
    path('books/page/<int:pk>/', book_detail, name='book-detail-page'),
]
