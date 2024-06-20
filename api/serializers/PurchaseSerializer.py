from rest_framework import serializers
from api.models import Purchase, Provider, Payment
from api.serializers.ProviderSerializer import ProviderSerializer
from api.serializers.PaymentSerializer import PaymentSerializer

class PurchaseSerializer(serializers.ModelSerializer):
    provider_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(), source='provider', write_only=True)
    payment_id = serializers.PrimaryKeyRelatedField(queryset=Payment.objects.all(), source='payment', write_only=True)
    provider_obj = ProviderSerializer(source='provider', read_only=True)
    payment_obj = PaymentSerializer(source='payment', read_only=True)

    class Meta:
        model = Purchase
        fields = ['id', 'date_purchase', 'number_bill', 'total', 'estatus', 'created_at', 'updated_at', 'provider_id', 'payment_id', 'provider_obj', 'payment_obj']

    def create(self, validated_data):
        provider = validated_data.pop('provider')
        payment = validated_data.pop('payment')
        purchase = Purchase.objects.create(provider=provider, payment=payment, **validated_data)
        return purchase