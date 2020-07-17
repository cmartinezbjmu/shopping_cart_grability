"""Products urls."""

# Django
from django.urls import path

# Views
from . import views

urlpatterns = [
    ##### Products #####

    # Product list
    path('',
         views.ProductsView.as_view({'get': 'list'}), name='products'),
    # Create product
    path('new',
         views.ProductsView.as_view({'post': 'create'}), name='create_product'),
    # Retrive product
    path('<int:pk>',
         views.ProductsView.as_view({'get': 'retrive'}), name='product'),
    # Update product
    path('update/<int:pk>', views.ProductsView.as_view({'patch': 'partial_update'}), name='update_product'),
    # Delete product
    path('delete/<int:pk>',
         views.ProductsView.as_view({'delete': 'destroy'}), name='delete_product'),
]
