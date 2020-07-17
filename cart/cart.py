"""Cart actions."""

# Django
from django.conf import settings

# Libraries
from rest_framework.response import Response


# Create your views here.
class Cart(object):
    """
        This class contain the businnes logic for add or remove products, increase o decrease items, 
        clear shopping cart and get detail of the cart.
    """

    # A cart that lives in the session
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, action=None):
        # Add or increment item
        id = product.id
        newItem = True
        # Add product if not exist in the cart
        if str(product.id) not in self.cart.keys():
            
            if product.amount_avaliable == 0:
                return "Don't have stock for this product"
            else:
                self.cart[product.id] = {
                    'product_id': id,
                    'name': product.name,
                    'quantity': 1,
                    'price': str(product.price),
                }
        else:
            # Increment item and validate stock
            newItem = True
            for key, value in self.cart.items():
                if key == str(product.id):
                    if (value['quantity'] + 1) > product.amount_avaliable:
                        return "Don't have more stock for this product"
                    else:
                        value['quantity'] = value['quantity'] + 1
                        newItem = False
                        self.save()
                        break
            # Create item if it has been deleted
            if newItem == True:
                self.cart[product.id] = {
                    'product_id': product.id,
                    'name': product.name,
                    'quantity': 1,
                    'price': str(product.price),
                }

        self.save()
        return self

    def save(self):
        # Update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        # Remove a product from the cart.
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        return self

    def decrement(self, product):
        # Decrement item
        for key, value in self.cart.items():
            if key == str(product.id):

                if(value['quantity'] < 2):
                    return self
                value['quantity'] = value['quantity'] - 1
                self.save()
                break
            else:
                print("Something Wrong")
        return self

    def clear(self):
        # Clear cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
        return self

    def total_price(self):
        # Total price cart
        price = float()
        for key, value in self.cart.items():
            partial_price = float(value['quantity']) * float(value['price'])
            price = price + partial_price
        return price
