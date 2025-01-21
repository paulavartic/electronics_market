from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from market.models import Supplier, Product, ChainUnit
from market.serializers import SupplierSerializer, ProductSerializer, ChainUnitSerializer, ChainUnitDetailSerializer
from users.permissions import IsActiveEmployee


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filterset_fields = ('country',)
    permission_classes = [IsAuthenticated, IsActiveEmployee]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,IsActiveEmployee]


class ChainUnitList(generics.ListAPIView):
    queryset = ChainUnit.objects.all()
    serializer_class = ChainUnitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('country', None)
        if country:
            queryset = queryset.filter(country=country)
        return queryset


class ChainUnitCreate(generics.CreateAPIView):
    queryset = ChainUnit.objects.all()
    serializer_class = ChainUnitSerializer
    permission_classes = [IsAuthenticated, IsActiveEmployee]


class ChainUnitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChainUnit.objects.all()
    serializer_class = ChainUnitDetailSerializer
    permission_classes = [IsAuthenticated, IsActiveEmployee]
