"""Users view."""

# Django
from django.shortcuts import render

# Libraries
from rest_framework import generics

# Models
from .models import CustomUser

# Serializers
from .serializers import UserSerializer


# Create your views here.

class UserListView(generics.ListAPIView):
    # Serializer user list
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer