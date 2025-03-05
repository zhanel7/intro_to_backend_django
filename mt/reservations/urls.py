from django.urls import path
from .views import *

urlpatterns = [
    path('', reservation_list, name='reservation-list'),
    path('<int:id>/', reservation_detail, name='reservation-detail'),
    path('create/', reservation_create, name='reservation-create'),
    path('<int:id>/update/', reservation_update, name='reservation-update'),
    path('<int:id>/delete/', reservation_delete, name='reservation-delete'),
]
