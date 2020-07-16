"""Cart views."""

# Django
from django.http import JsonResponse

# Libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets

# Local methods
from .cart import Cart

# Models
from products.models import Product

# Create your views here.

class CartView(viewsets.ViewSet):

    # Add products to shopping cart
    def add(self, request, pk):
        cart = Cart(request)
        product = Product.objects.get(id=pk)
        respuesta = cart.add(product=product)
        return JsonResponse(respuesta.session['cart'])


