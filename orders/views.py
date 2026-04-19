from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

@api_view(['POST'])
def create_order(request):
    data = request.data
    serializer = OrderSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Order created"})
    
    return Response(serializer.errors)