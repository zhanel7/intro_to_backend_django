from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("add/", views.todo_add, name="todo_add"),
    path("edit/<int:pk>/", views.todo_edit, name="todo_edit"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete"),
    path("todo/<int:pk>/", views.todo_detail, name="todo_detail"),
]
