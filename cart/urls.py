"""Cart urls."""

# Djgango
from django.urls import path

# Views
from . import views

urlpatterns = [
    path('api/v1/cart/add/<int:pk>/', views.CartView.as_view({'post': 'add'}), name='card_add'),
    path('api/v1/cart/remove/<int:pk>/', views.CartView.as_view({'post': 'remove'}), name='card_remove'),
]