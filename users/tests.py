from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from django.shortcuts import render
import json
from rest_framework import status
# Create your tests here.

class UsersTestCase(TestCase):
    def setUp(self):
        self.valid_user_register = {
            'username': 'Grability',
            'password1': 'Grability2020*',
            'password2': 'Grability2020*'
        }
        self.invalid_user_register = {
            'username': 'Grability',
            'password1': 'Grability2020',
            'password2': 'Grability2020*'
        }
        self.valid_user_login = {
            'username': 'Grability',
            'password': 'Grability2020*'
        }

    def test_valid_user_register(self):
        response = self.client.post(
            reverse('rest_register'),
            data=json.dumps(self.valid_user_register),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_invalid_user_register(self):
        response = self.client.post(
            reverse('rest_register'),
            data=json.dumps(self.invalid_user_register),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_valid_user_login(self):

        response = self.client.post(
            reverse('rest_register'),
            data=json.dumps(self.valid_user_register),
            content_type='application/json'
        )

        response = self.client.post(
            reverse('rest_login'),
            data=json.dumps(self.valid_user_login),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)