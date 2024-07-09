from rest_framework import serializers
from api.models import Purchase, Provider,DetailPurchase
from api.serializers.ProviderSerializer import ProviderSerializer
from api.serializers.DetailPurchaseSerializer import DetailPurchaseSerializer

class PurchaseSerializer(serializers.ModelSerializer):
    provider_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), source='provider', write_only=True)
    provider_obj = ProviderSerializer(source='provider', read_only=True)
    detailpurchase_id = serializers.PrimaryKeyRelatedField(queryset=DetailPurchase.objects.all(), source='detailpurchase', write_only=True)
    detailpurchase_obj = DetailPurchaseSerializer(source='detailpurchase', read_only=True)
    class Meta:
        model = Purchase
        fields = ['id', 'description', 'date_purchase', 'number_bill', 'total', 'estatus', 'created_at', 'updated_at', 'provider_id', 'provider_obj', 'detailpurchase_id','detailpurchase_obj']

    def create(self, validated_data):
        provider = validated_data.pop('provider')
        detailpurchase = validated_data.pop('detailpurchase')
        purchase = Purchase.objects.create(provider=provider,detailpurchase=detailpurchase, **validated_data)
        return purchase