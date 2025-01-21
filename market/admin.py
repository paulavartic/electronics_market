from django.contrib import admin
from market.models import Supplier, Product, ChainUnit


@admin.action(description='Clearing debt to supplier')
def clear_debt(modeladmin, request, queryset):
    for unit in queryset:
        unit.debt_to_supplier = 0.00
        unit.save()


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')


@admin.register(ChainUnit)
class ChainUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city', 'supplier', 'debt_to_supplier', 'created_at', 'level')
    search_fields = ('name', 'city',)
    list_filter = ('city',)
    actions = [clear_debt]

    def get_supplier_link(self, obj):
        if obj.supplier:
            return f'<a href="/admin/app_name/chainunit/{obj.supplier.id}/change/">{obj.supplier.name}</a>'
        return 'No supplier'

    get_supplier_link.short_description = "Supplier"
    get_supplier_link.allow_tags = True
