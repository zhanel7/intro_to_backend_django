from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Добро пожаловать в Django API!</h1><p>Используйте /movies/ и /articles/ для работы с API.</p>")