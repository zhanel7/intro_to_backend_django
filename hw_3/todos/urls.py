from django.urls import path
from .views import todo_list_view, create_todo, delete_todo, TodoListView, TodoDetailView

urlpatterns = [
    # HTML-страницы
    path('', todo_list_view, name='todo_list'),
    path('create/', create_todo, name='create_todo'),
    path('<int:id>/delete/', delete_todo, name='delete_todo'),

    # API эндпоинты
    path('api/todos/', TodoListView.as_view(), name='api_todos'),
    path('api/todos/<int:pk>/', TodoDetailView.as_view(), name='api_todo_detail'),
]
