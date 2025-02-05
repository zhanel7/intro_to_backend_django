from django.shortcuts import render
from .models import Book

def book_list_page(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
        return render(request, 'book/book_detail.html', {'book': book})
    except Book.DoesNotExist:
        return render(request, 'book/book_not_found.html')
