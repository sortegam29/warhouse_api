from rest_framework import serializers
from .models import Product, Category, ProductVariant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'description', 'category', 'unit_type', 'created_at', 'updated_at']


class ProductVariantSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product'
    )

    class Meta:
        model = ProductVariant
        fields = ['id', 'product', 'product_id', 'sku', 'attributes', 'created_at', 'updated_at']