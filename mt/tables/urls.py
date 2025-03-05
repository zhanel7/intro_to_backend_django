from django.urls import path
from .views import *

urlpatterns = [
    path('', table_list, name='table-list'),
    path('<int:id>/', table_detail, name='table-detail'),
    path('create/', table_create, name='table-create'),
    path('<int:id>/update/', table_update, name='table-update'),
    path('<int:id>/delete/', table_delete, name='table-delete'),
]
