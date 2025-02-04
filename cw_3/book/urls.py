from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetail.as_view(), name='book-detail'),
]

from book import views as book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_views.book_list_page),  # Для отображения списка книг
]
