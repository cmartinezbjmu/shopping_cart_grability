from django.contrib import admin
from .models import CustomUser

# Register your models here.
models = [CustomUser]
admin.site.register(models)