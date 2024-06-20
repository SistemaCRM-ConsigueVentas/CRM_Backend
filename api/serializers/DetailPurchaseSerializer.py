from rest_framework import serializers
from api.models import DetailPurchase

class DetailPurchaseSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = DetailPurchase
        fields = ['id', 'date_purchase', 'item', 'price', 'quantity', 'total', 'purchase_id']