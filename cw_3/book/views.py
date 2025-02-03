from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = list(Book.objects.values())
    return JsonResponse({'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return JsonResponse({'book': book})
from django.shortcuts import render

# Create your views here.
