"""Cart views."""

# Django
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404

# Libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Local methods
from .cart import Cart

# Models
from products.models import Product


# Create your views here.

class CartView(viewsets.ViewSet):
    """
        This class contain methods for add or remove products, increase o decrease items, 
        clear shopping cart and get detail of the cart.
    """

    # Add products to the shopping cart
    def item_add(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        if product:
            cart_list = cart.add(product=product)
            try:
                if cart_list.session[settings.CART_SESSION_ID]:
                    return JsonResponse(cart_list.session[settings.CART_SESSION_ID], status=status.HTTP_200_OK)
            except:
                return Response({'detail': cart_list}, status=status.HTTP_200_OK)
    
        return Response({'detail': 'This product don´t exist'}, status=status.HTTP_204_NO_CONTENT)

    # remove products to the shopping cart
    def item_remove(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        if product:
            cart_list = cart.remove(product)
            return JsonResponse(cart_list.session[settings.CART_SESSION_ID], status=status.HTTP_200_OK)

    # Increment quantity of items in the shopping cart
    def item_increment(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        if product:
            cart_list = cart.add(product=product)
            try:
                if cart_list.session[settings.CART_SESSION_ID]:
                    return JsonResponse(cart_list.session[settings.CART_SESSION_ID], status=status.HTTP_200_OK)
            except:
                return Response({'detail': cart_list}, status=status.HTTP_200_OK)

    # Decrement quantity of items in the shopping cart
    def item_decrement(self, request, pk):
        cart = Cart(request)
        
        product = get_object_or_404(Product, id=pk)
        if product:
            cart_list = cart.decrement(product=product)
            return JsonResponse(cart_list.session[settings.CART_SESSION_ID], status=status.HTTP_200_OK)

    # Clear de shopping cart
    def cart_clear(self, request):
        cart = Cart(request)
        cart_list = cart.clear()
        return Response({'detail': 'Your products have been removed'}, status=status.HTTP_200_OK)

    # Retrive list of items
    def cart_detail(self, request):
        return JsonResponse(request.session[settings.CART_SESSION_ID], status=status.HTTP_200_OK)

    def total_price(self, request):
        cart = Cart(request)
        total_price = cart.total_price()
        print(total_price)
        return JsonResponse({'total_price': total_price}, status=status.HTTP_200_OK)