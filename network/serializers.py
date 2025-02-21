from rest_framework import serializers

from network.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализатор поставщиков."""
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ('debt',)
