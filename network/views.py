from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from network.models import Supplier
from network.permissions import IsActiveEmployee
from network.serializers import SupplierSerializer


class SupplierViewSet(ModelViewSet):
    """ViewSet для работы с поставщиками."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [SearchFilter]
    search_fields = ['country']


