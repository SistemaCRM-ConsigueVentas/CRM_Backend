from rest_framework import serializers
from api.models import Purchase, Provider
from api.serializers.ProviderSerializer import ProviderSerializer

class PurchaseSerializer(serializers.ModelSerializer):
    provider_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), source='provider', write_only=True)
    provider_obj = ProviderSerializer(source='provider', read_only=True)

    class Meta:
        model = Purchase
        fields = ['id', 'date_purchase', 'number_bill', 'total', 'estatus', 'created_at', 'updated_at', 'provider_id', 'provider_obj']

    def create(self, validated_data):
        provider = validated_data.pop('provider')
        purchase = Purchase.objects.create(provider=provider, **validated_data)
        return purchase