"""Users urls."""

# Django
from django.urls import include, path

# Views
from .views import UserListView

urlpatterns = [
    ##### USERS ######
    
    # Rest framewor user login, logout, user update, password change and password reset
    path('rest-auth/', include('rest_auth.urls')),
    # Rest framework user register
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # List of users
    path('', UserListView.as_view()),
]
