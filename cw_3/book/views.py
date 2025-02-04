from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all().values('id', 'title', 'author', 'description', 'publication_year')
    return JsonResponse(list(books), safe=False)

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
        return JsonResponse({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'description': book.description,
            'publication_year': book.publication_year
        })
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

def book_list_page(request):
    books = Book.objects.all()
    return render(request, 'book/books.html', {'books': books})
