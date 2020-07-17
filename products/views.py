"""Products views."""

# Django
from django.shortcuts import render, get_object_or_404

# Libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Models
from .models import Product

# Serializers
from .serializers import ProductsSerializer

# Create your views here.


class ProductsView(viewsets.ModelViewSet):
    """Products view."""
    serializer_class = ProductsSerializer

    # Get list of products
    def get_queryset(self):
        return Product.objects.filter()

    # Create a new product
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Get a specific product by id
    def retrive(self, request, pk=None, **kwargs):
        product = get_object_or_404(Product, id=pk)
        product_serializer = ProductsSerializer(product)
        return Response({'product': product_serializer.data})

    # Update a specific product by id
    def update(self, request, pk=None, **kwargs):
        product = get_object_or_404(Product, id=pk)
        partial = kwargs.pop('partial', False)
        serializer = ProductsSerializer(
            product, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # Delete a specific product by id
    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, id=pk)
        self.perform_destroy(product)
        return Response({'detail': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)
