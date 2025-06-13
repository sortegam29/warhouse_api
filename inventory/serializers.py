from rest_framework import serializers
from .models import Inventory
from products.serializers import ProductSerializer
from warehouses.serializers import WarehouseSerializer

class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    warehouse = WarehouseSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'warehouse', 'quantity', 'minimum_stock', 'created_at', 'updated_at']