from rest_framework import serializers
from api.models import DetailPurchase, Purchase
from api.serializers.PurchaseSerializer import PurchaseSerializer

class DetailPurchaseSerializer(serializers.ModelSerializer):
    purchase_id = serializers.PrimaryKeyRelatedField(queryset=Purchase.objects.all(), source='purchase', write_only=True)
    purchase_obj = PurchaseSerializer(source='purchase', read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = DetailPurchase
        fields = ['id', 'date_purchase', 'item', 'price', 'quantity', 'total','description', 'purchase_id','purchase_obj']
    
    def create(self, validated_data):
        purchase = validated_data.pop('purchase')
        detail_purchase = DetailPurchase.objects.create(purchase=purchase, **validated_data)
        return detail_purchase