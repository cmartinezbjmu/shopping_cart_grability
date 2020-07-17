"""Order views."""

# Models
from .models import OrderItem, Order

# Local methods
from cart.cart import Cart
from .orders import Orders

# Libraries
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.

class OrderView(viewsets.ViewSet):
    # Created order
    permission_classes = (IsAuthenticated,)
    
    def create_order(self, request):
        order = Orders(request)
        response_stock, status_code_stock, flag = order.stock_validate()
        if flag == False:
            response_create, status_code = order.order_create()
            cart = Cart(request)
            cart_list = cart.clear()
            return Response({'detail': response_create}, status=status_code)
        else:
            return Response({'detail': response_stock}, status=status_code_stock)
