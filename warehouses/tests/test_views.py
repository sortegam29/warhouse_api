from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .test_models import Warehouse

class LocationAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.warehouse = Warehouse.objects.create(code="WH001", name="Main Warehouse", address="Address 1")

    def test_create_location(self):
        data = {
            "warehouse_id": self.warehouse.id,
            "code": "WH001-A1",
            "name": "Shelf A1"
        }
        response = self.client.post("/api/locations/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["code"], "WH001-A1")