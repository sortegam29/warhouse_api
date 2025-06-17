from django.test import TestCase
from warehouses.models import Location, Warehouse

class LocationModelTest(TestCase):
    def test_create_nested_location(self):
        warehouse = Warehouse.objects.create(code="WH001", name="Main Warehouse", address="Address 1")
        parent = Location.objects.create(warehouse=warehouse, code="WH001-A", name="Zone A")
        child = Location.objects.create(warehouse=warehouse, code="WH001-A1", name="Shelf A1", parent=parent)
        self.assertEqual(child.parent.name, "Zone A")