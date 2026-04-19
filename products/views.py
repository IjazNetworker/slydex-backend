from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# ✅ Get all products (with brand filter)
@api_view(['GET'])
def get_products(request):
    brand = request.GET.get('brand')

    if brand:
        products = Product.objects.filter(brand=brand)
    else:
        products = Product.objects.all()

    data = []
    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "brand": product.brand,
            "sales_price": product.Sales_price,
            "cost_price": product.Cost_price,
            "image": product.image.url,
            "stock": product.stock,
            "whatsapp_number": product.whatsapp_number
        })

    return Response(data)


# ✅ Get unique brands
@api_view(['GET'])
def get_brands(request):
    brands = Product.objects.values_list('brand', flat=True).distinct()
    return Response(brands)


@api_view(['GET'])
def get_product_detail(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)