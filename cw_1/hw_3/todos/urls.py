from django.urls import path
from .views import todo_list, todo_detail, todo_create, todo_delete, todo_update

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('<int:id>/', todo_detail, name='todo_detail'),  # Открытие деталей задачи
    path('<int:id>/edit/', todo_update, name='todo_edit'),  # Редактирование задачи
    path('create/', todo_create, name='create_todo'),
    path('<int:id>/delete/', todo_delete, name='delete_todo'),
]
