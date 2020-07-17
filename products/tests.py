from django.test import TestCase
from products.models import Product
from django.urls import reverse
from django.core.files import File
import tempfile

# Create your tests here.

image = tempfile.NamedTemporaryFile(suffix=".jpg").name

class ProductsTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='Manzana', price=900, amount_avaliable=14)
        Product.objects.create(name='Pera', price=1500, amount_avaliable=20, image=image)

    def test_list_products(self):
        response = self.client.get(reverse('products'), formal='json')
        self.assertEqual(response.status_code, 200)