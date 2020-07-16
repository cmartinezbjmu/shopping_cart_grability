"""Products urls."""

# Django
from django.urls import path

# Views
from . import views

urlpatterns = [
    ##### Products #####

    # Product list
    path('api/v1/products',
         views.ProductsView.as_view({'get': 'list'}), name='products'),
    # Create product
    path('api/v1/products/new',
         views.ProductsView.as_view({'post': 'create'}), name='create_product'),
    # Retrive product
    path('api/v1/products/<int:pk>',
         views.ProductsView.as_view({'get': 'retrive'}), name='product'),
    # Update product
    path('api/v1/products/update/<int:pk>', views.ProductsView.as_view({'patch': 'partial_update'}), name='update_product'),
    # Delete product
    path('api/v1/products/delete/<int:pk>',
         views.ProductsView.as_view({'delete': 'destroy'}), name='delete_product'),
]
