from rest_framework import viewsets
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]