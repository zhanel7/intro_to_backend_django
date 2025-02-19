from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('todo-lists/', views.todo_lists_view, name='todo_lists'),
    path('todo-lists/<int:id>/', views.todo_list_detail_view, name='todo_list_detail'),
    path('todo-lists/<int:id>/delete/', views.todo_list_delete_view, name='todo_list_delete'),
    path('todo-lists/<int:id>/edit/', views.todo_list_edit_view, name='todo_list_edit'),
    path('todos/<int:id>/delete/', views.todo_delete_view, name='todo_delete'),
    path('todos/<int:id>/edit/', views.todo_edit_view, name='todo_edit'),
]
