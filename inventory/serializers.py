from rest_framework import serializers
from .models import Inventory, Product, Location, InventoryMovement, Batch
from products.serializers import ProductSerializer
from warehouses.serializers import WarehouseSerializer, LocationSerializer
from decimal import Decimal, InvalidOperation

class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    warehouse = WarehouseSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'warehouse', 'quantity', 'minimum_stock', 'created_at', 'updated_at']


class InventoryMovementSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')
    from_location = LocationSerializer(read_only=True)
    from_location_id = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), source='from_location', required=False)
    to_location = LocationSerializer(read_only=True)
    to_location_id = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), source='to_location', required=False)

    class Meta:
        model = InventoryMovement
        fields = ['id', 'movement_type', 'product', 'product_id', 'from_location', 'from_location_id', 'to_location', 'to_location_id', 'quantity', 'reason', 'user', 'created_at']
    
    def validate_quantity(self, value):
        try:
            # Asegura que sea un número válido
            return Decimal(value)
        except (InvalidOperation, TypeError, ValueError):
            raise serializers.ValidationError("El valor debe ser un número decimal.")
        
class BatchSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')

    class Meta:
        model = Batch
        fields = ['id', 'product', 'product_id', 'lot_number', 'expiration_date', 'manufacture_date', 'quantity', 'location', 'created_at']