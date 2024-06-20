from api.model.PaymentModel import *
from rest_framework import serializers
from api.models import Purchase, Payment
from api.serializers.PurchaseSerializer import PurchaseSerializer

class PaymentSerializer(serializers.ModelSerializer):    
    purchase_id = serializers.PrimaryKeyRelatedField(queryset=Purchase.objects.all(), source='purchase', write_only=True)
    purchase_obj = PurchaseSerializer(source='purchase', read_only=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'date_payment', 'date_limit', 'payment_method', 'total', 'cancelled_total', 'estatus', 'purchase_id', 'purchase_obj']

    def create(self, validated_data):
        purchase = validated_data.pop('purchase')
        payment = Payment.objects.create(purchase=purchase, **validated_data)
        return payment