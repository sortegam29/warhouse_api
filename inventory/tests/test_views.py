from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from inventory.models import Warehouse, Location, Product

class InventoryMovementAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.product = Product.objects.create(sku="PROD001", name="Base Product", unit_type="unit")
        self.warehouse = Warehouse.objects.create(code="WH001", name="Main Warehouse", address="Address 1")
        self.location = Location.objects.create(warehouse=self.warehouse, code="WH001-A1", name="Shelf A1")

    def test_invalid_quantity_rejected(self):
        data = {
            "movement_type": "in",
            "product_id": self.product.id,
            "to_location_id": self.location.id,
            "quantity": "hundred",
            "reason": "Invalid quantity test"
        }
        response = self.client.post("/api/movements/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("quantity", response.data)