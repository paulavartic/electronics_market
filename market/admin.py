from django.contrib import admin
from market.models import Supplier, Product, ChainUnit


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(ChainUnit)
class ChainUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
