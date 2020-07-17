from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from django.shortcuts import render
import json
from rest_framework import status
from products.models import Product
# Create your tests here.

class CartTestCase(TestCase):
    def setUp(self):
        self.manzana = Product.objects.create(name='Manzana', price=900, amount_avaliable=14)
        self.pera = Product.objects.create(name='Pera', price=1500, amount_avaliable=20)

    def test_valid_add_product(self):
        response = self.client.post(
            reverse('card_add', kwargs={'pk': self.manzana.pk}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_increment_product(self):
        response = self.client.post(
            reverse('card_increment', kwargs={'pk': self.manzana.pk}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_decrement_product(self):
        response = self.client.post(
            reverse('card_decrement', kwargs={'pk': self.manzana.pk}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_cart_clear(self):
        response = self.client.get(reverse('cart_clear'), formal='json')
        self.assertEqual(response.status_code, 200)   

    def test_valid_remove_product(self):
        response = self.client.post(
            reverse('card_remove', kwargs={'pk': self.manzana.pk}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

