
"""Products models."""

# Django
from django.db import models

class Product(models.Model):
    """Products model."""
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount_avaliable = models.PositiveIntegerField(default=1)