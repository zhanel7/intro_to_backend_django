from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# 🔹 API Views (JSON)
class BookListView(generics.ListAPIView):
    """Вывод списка всех книг в формате JSON"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    """Вывод информации о конкретной книге по ID в формате JSON"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# 🔹 HTML Views (Страницы)
def book_list(request):
    """Вывод списка книг на HTML-странице"""
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, pk):
    """Вывод информации о конкретной книге на HTML-странице"""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})
