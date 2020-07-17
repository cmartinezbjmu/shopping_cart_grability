"""Order urls."""

# Django
from django.urls import path

# Views
from . import views

urlpatterns = [
    path('', views.OrderView.as_view(
        {'get': 'create_order'}), name='order-create'),
]
