from django.urls import path
from .views import get_products, get_product_detail,get_brands

urlpatterns = [
    path('', get_products),
    path('<int:id>/', get_product_detail),
    path('brands/', get_brands),
]