"""User serializers."""

# Libraries
from rest_framework import serializers

# Models
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', )
        
