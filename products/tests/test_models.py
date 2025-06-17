from django.test import TestCase
from products.models import Product, Category

class ProductModelTest(TestCase):
    def test_create_product_with_valid_sku(self):
        category = Category.objects.create(name="Electronics", slug="electronics")
        product = Product.objects.create(
            sku="PROD001",
            name="Test Product",
            category=category,
            unit_type="unit"
        )
        self.assertEqual(product.sku, "PROD001")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.category.name, "Electronics")

    def test_product_sku_must_be_unique(self):
        Category.objects.create(name="Electronics", slug="electronics")
        Product.objects.create(sku="PROD001", name="Test Product", unit_type="unit")
        with self.assertRaises(Exception):  # Debería lanzar IntegrityError
            Product.objects.create(sku="PROD001", name="Duplicate SKU", unit_type="unit")

from products.models import ProductVariant

class ProductVariantModelTest(TestCase):
    def test_create_variant_with_attributes(self):
        category = Category.objects.create(name="Electronics", slug="electronics")
        product = Product.objects.create(sku="PROD001", name="Base Product", category=category, unit_type="unit")
        variant = ProductVariant.objects.create(
            product=product,
            sku="PROD001-RED-M",
            attributes={"color": "red", "size": "M"}
        )
        self.assertEqual(variant.attributes["color"], "red")
        self.assertEqual(variant.sku, "PROD001-RED-M")