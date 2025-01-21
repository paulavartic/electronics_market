from rest_framework.serializers import ModelSerializer

from market.models import Supplier, Product, ChainUnit


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['debt']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ChainUnitSerializer(ModelSerializer):
    class Meta:
        model = ChainUnit
        fields = '__all__'
        read_only_fields = ('debt_to_supplier',)


class ChainUnitDetailSerializer(ModelSerializer):
    class Meta:
        model = ChainUnit
        fields = ('name', 'level', 'supplier', 'debt_to_supplier',)
