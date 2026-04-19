from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

# ✅ Create Order
@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# ✅ Get Orders (with filter)
@api_view(['GET'])
def get_orders(request):
    status_param = request.GET.get('status')

    if status_param:
        orders = Order.objects.filter(status=status_param)
    else:
        orders = Order.objects.all()

    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


# ✅ Update Order Status
@api_view(['PUT'])
def update_order(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = OrderSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)