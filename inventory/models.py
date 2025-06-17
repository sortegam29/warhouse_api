from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from warehouses.models import Location
from warehouses.models import Warehouse

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    minimum_stock = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'warehouse')

    def __str__(self):
        return f"{self.product.sku} @ {self.warehouse.code} - {self.quantity}"
    

class InventoryMovement(models.Model):
    MOVEMENT_TYPES = [
        ('in', 'Entrada'),
        ('out', 'Salida'),
        ('transfer', 'Traslado'),
        ('adjustment', 'Ajuste'),
    ]
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='from_movements')
    to_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='to_movements')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    reason = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    lot_number = models.CharField(max_length=50)
    expiration_date = models.DateField(null=True, blank=True)
    manufacture_date = models.DateField(null=True, blank=True)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)