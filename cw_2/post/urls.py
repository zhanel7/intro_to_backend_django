from django.urls import path
from .views import post_list, post_detail, post_create, post_delete

urlpatterns = [
    path('', post_list, name='post-list'),  # GET posts/
    path('<int:id>/', post_detail, name='post-detail'),  # GET posts/:id
    path('create/', post_create, name='post-create'),  # POST posts/
    path('<int:id>/delete/', post_delete, name='post-delete'),  # DELETE posts/:id/delete
]
