from rest_framework import serializers
from api.model.SaleDetailsServiceModel import SaleDetailsService
from api.model.SaleModel import Sale
from api.serializers.SaleSerializer import SaleSerializer
from api.serializers.ServiceSerializer import ServiceSerializer

class SaleDetailsServiceSerializer(serializers.ModelSerializer):
    sale = SaleSerializer(read_only = True)
    service = ServiceSerializer(read_only = True)
    tax = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    total_item_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = SaleDetailsService
        fields = ['id', 'quantity', 'unit_price', 'discount', 'tax', 'total_item_amount', 'created_at', 'sale', 'service']
        
    def get_sale_data(self, obj):
        sale = obj.sale 
        sale_serializer = SaleSerializer(sale)
        return sale_serializer.data

    def create(self, validated_data):
        total_item_amount = (validated_data['quantity'] * validated_data['unit_price']) - validated_data['discount']
        validated_data['total_item_amount'] = total_item_amount + (total_item_amount * SaleDetailsService.TAX_RATE)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.unit_price = validated_data.get('unit_price', instance.unit_price)
        instance.discount = validated_data.get('discount', instance.discount)
        
        # Recalculamos total_item_amount automáticamente
        total_item_amount = (instance.quantity * instance.unit_price) - instance.discount
        instance.total_item_amount = total_item_amount + (total_item_amount * SaleDetailsService.TAX_RATE)
        
        # Actualizamos Sale si se proporciona
        sale_data = validated_data.pop('sale', None)
        if sale_data:
            instance.sale = sale_data
        
        # Actualizamos Service si se proporciona 
        service_data = validated_data.pop('service', None)
        if service_data:
            instance.service = service_data
        
        instance.save()
        return instance
