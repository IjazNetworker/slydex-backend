from rest_framework import serializers
from .models import Order
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image']


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    product_details = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'