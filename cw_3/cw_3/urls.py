from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Book Review API</h1>")

urlpatterns = [
    path('', home),  # 👈 Добавлен корневой маршрут
    path('admin/', admin.site.urls),
    path('api/', include('book.urls')),
    path('api/', include('review.urls')),
]
