"""Products serializers."""

# Django rest framework
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

# Models
from .models import Product


class ProductsSerializer(serializers.ModelSerializer):
    """Products serializer."""
    # Serializer all fields of model
    class Meta:
        model = Product
        fields = '__all__'