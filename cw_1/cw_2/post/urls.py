from django.urls import path
from .views import post_list, post_detail, post_create, post_delete

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
    path('<int:post_id>/delete/', post_delete, name='post_delete'),
]
