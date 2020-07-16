
"""Products models."""

# Django
from django.db import models

class Product(models.Model):
    """Products model."""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.FloatField()
    amount_avaliable = models.FloatField()