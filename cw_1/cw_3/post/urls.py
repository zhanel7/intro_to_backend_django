from django.urls import path
from . import views

urlpatterns = [
    path('', views.thread_list, name='thread_list'),  # /threads/
    path('create/', views.thread_create, name='thread_create'),  # /threads/create/
    path('<int:thread_id>/', views.thread_detail, name='thread_detail'),  # /threads/1/
    path('<int:thread_id>/delete/', views.thread_delete, name='thread_delete'),  # /threads/1/delete/
    path('<int:thread_id>/post/create/', views.post_create, name='post_create'),  # /threads/1/post/create/
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),  # /post/1/delete/
]
