from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AuthAPITest(APITestCase):
    def test_obtain_jwt_token(self):
        User.objects.create_user(username="testuser", password="testpass")
        data = {
            "username": "testuser",
            "password": "testpass"
        }
        response = self.client.post("/api/token/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_access_protected_endpoint_without_token(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)