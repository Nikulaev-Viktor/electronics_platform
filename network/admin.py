from django.contrib import admin, messages

from network.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'country', 'city', 'street', 'level', 'debt', 'supplier')
    search_fields = ('name', 'email', 'country', 'city', 'street', 'house_number', 'supplier__name')
    list_filter = ('city',)
    ordering = ('-created_at',)
    actions = ['clear_debt']
    list_display_links = ('supplier', 'name')
    list_per_page = 10

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        count = queryset.update(debt=0)
        self.message_user(request, f'Задолженность перед поставщиком была очищена у {count} объектов',
                          messages.ERROR)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'model', 'supplier', 'release_date')
    search_fields = ('product_name', 'model', 'supplier__name')
    list_filter = ('supplier', 'release_date')
    ordering = ('-release_date',)
    list_display_links = ('supplier', 'product_name')
    list_per_page = 10
