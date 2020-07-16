"""Cart views."""

# Django
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings

# Models
from products.models import Product


# Create your views here.
class Cart(object):
    
    def __init__(self, request):
        #import pdb; pdb.set_trace()
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, action=None):
        id = product.id
        newItem = True
        if str(product.id) not in self.cart.keys():

            self.cart[product.id] = {
                'product_id': id,
                'name': product.name,
                'quantity': 1,
                'price': str(product.price),
                'image': product.image.url
            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.id):

                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[product.id] = {
                    'product_id': product.id,
                    'name': product.name,
                    'quantity': 1,
                    'price': str(product.price),
                    'image': product.image.url
                }

        self.save()
        return self

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


