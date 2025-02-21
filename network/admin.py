from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html

from network.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'country', 'city', 'street', 'level', 'debt', 'supplier_link')
    search_fields = ('name', 'email', 'country', 'city', 'street', 'house_number', 'supplier__name')
    list_filter = ('city',)
    ordering = ('-created_at',)
    actions = ['clear_debt']
    list_display_links = ('id', 'name')
    list_per_page = 10
    readonly_fields = ('supplier_link',)

    def supplier_link(self, obj):
        """Создаёт ссылку на страницу редактирования поставщика в админке."""
        if obj.supplier:
            url = reverse("admin:network_supplier_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "—"

    supplier_link.short_description = "Ссылка на поставщика"

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
