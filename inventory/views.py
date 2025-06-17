from rest_framework import viewsets
from .models import Inventory, InventoryMovement, Batch
from .serializers import InventorySerializer, InventoryMovementSerializer, BatchSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class InventoryMovementViewSet(viewsets.ModelViewSet):
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        movement = serializer.save(user=self.request.user)
        if movement.movement_type == 'in':
            Inventory.objects.update_or_create(
                product=movement.product,
                warehouse=movement.to_location.warehouse,
                defaults={'quantity': ...}
            )
        elif movement.movement_type == 'out':
            ...


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]