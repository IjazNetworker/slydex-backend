from django.urls import path
from .views import create_order, get_orders, update_order

urlpatterns = [
    path('', get_orders),
    path('create/', create_order),
    path('<int:pk>/', update_order),
]