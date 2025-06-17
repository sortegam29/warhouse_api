from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .test_models import Product

class ProductAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_get_products_list(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        data = {
            "sku": "PROD002",
            "name": "New Product",
            "unit_type": "unit"
        }
        response = self.client.post("/api/products/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["sku"], "PROD002")

class ProductVariantAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.product = Product.objects.create(sku="PROD001", name="Base Product", unit_type="unit")

    def test_create_product_variant(self):
        data = {
            "product_id": self.product.id,
            "sku": "PROD001-RED-M",
            "attributes": {"color": "red", "size": "M"}
        }
        response = self.client.post("/api/product-variants/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["sku"], "PROD001-RED-M")