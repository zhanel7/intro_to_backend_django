from django.urls import path
from .views import *

urlpatterns = [
    path('', customer_list, name='customer-list'),
    path('<int:id>/', customer_detail, name='customer-detail'),
    path('create/', customer_create, name='customer-create'),
    path('<int:id>/update/', customer_update, name='customer-update'),
    path('<int:id>/delete/', customer_delete, name='customer-delete'),
]
