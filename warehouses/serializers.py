from rest_framework import serializers
from .models import Warehouse, Location

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'code', 'name', 'address', 'created_at', 'updated_at']

class LocationSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)
    warehouse_id = serializers.PrimaryKeyRelatedField(
        queryset=Warehouse.objects.all(), source='warehouse'
    )

    class Meta:
        model = Location
        fields = ['id', 'warehouse', 'warehouse_id', 'parent', 'code', 'name', 'description', 'created_at', 'updated_at']