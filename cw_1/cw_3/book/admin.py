# book/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Отображаем поля в списке
    search_fields = ('title', 'author')  # Добавляем возможность поиска по этим полям
