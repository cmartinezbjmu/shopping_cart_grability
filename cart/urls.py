"""Cart urls."""

# Djgango
from django.urls import path

# Views
from . import views

urlpatterns = [
    ###### CART ######
    path('add/<int:pk>/',
         views.CartView.as_view({'post': 'item_add'}), name='card_add'),
    path('remove/<int:pk>/',
         views.CartView.as_view({'post': 'item_remove'}), name='card_remove'),
    path('increment/<int:pk>/',
         views.CartView.as_view({'post': 'item_increment'}), name='card_increment'),
    path('decrement/<int:pk>/',
         views.CartView.as_view({'post': 'item_decrement'}), name='card_decrement'),
    path(
        'clear/', views.CartView.as_view({'get': 'cart_clear'}), name='cart_clear'),
    path(
        'detail/', views.CartView.as_view({'get': 'cart_detail'}), name='cart_detail'),
    path(
        'total_price/', views.CartView.as_view({'get': 'total_price'}), name='total_price'),
]
