from rest_framework import serializers
from api.model.SaleDetailsServiceModel import SaleDetailsService

class SaleDetailsServiceSerializer(serializers.ModelSerializer):
    tax = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    total_item_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = SaleDetailsService
        fields = ['id', 'quantity', 'unit_price', 'discount', 'tax', 'total_item_amount', 'created_at', 'sale', 'service']

    def create(self, validated_data):
        total_item_amount = (validated_data['quantity'] * validated_data['unit_price']) - validated_data['discount']
        validated_data['total_item_amount'] = total_item_amount + (total_item_amount * SaleDetailsService.TAX_RATE)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Actualiza los datos del objeto
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.unit_price = validated_data.get('unit_price', instance.unit_price)
        instance.discount = validated_data.get('discount', instance.discount)
        
        # Recalcula el total_item_amount automáticamente
        total_item_amount = (instance.quantity * instance.unit_price) - instance.discount
        instance.total_item_amount = total_item_amount + (total_item_amount * SaleDetailsService.TAX_RATE)
        
        instance.save()
        return instance