from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from network.models import NetworkElement, Product
from network.serializers import NetworkElementSerializer, ProductSerializer

# Create your views here.


class NetworkElementViewSet(viewsets.ModelViewSet):
    """API для работы с элементами сети"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()

    def perform_create(self, serializer):
        if 'debt_to_supplier' in serializer.validated_data:
            raise PermissionDenied('Обновление задолженности запрещено.')
        super().perform_update(serializer)

    def get_queryset(self):
        queryset = NetworkElement.objects.all()
        country = self.request.query_param(country=country)
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    """API для работы с продуктами"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
