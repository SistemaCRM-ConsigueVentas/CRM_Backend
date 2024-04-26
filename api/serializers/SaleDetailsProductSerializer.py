from rest_framework import serializers
from api.models import SaleDetailsProduct, Sale, Product
from .SaleSerializer import SaleSerializer
from .ProductSerializer import ProductSerializer
from decimal import Decimal

class SaleDetailsProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    
    sale_obj = SaleSerializer(source='sale', read_only=True)
    sale = serializers.PrimaryKeyRelatedField(queryset=Sale.objects.all(), write_only=True)
    
    product_obj = ProductSerializer(source='product', read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    
    tax = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    total_item_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = SaleDetailsProduct
        fields = ['id', 'quantity', 'unit_price', 'discount', 'tax', 'total_item_amount', 'created_at', 'sale_obj', 'product_obj', 'product','sale']

    def create(self, validated_data):
        sale = validated_data.pop('sale')
        total_item_amount = (validated_data['quantity'] * validated_data['unit_price']) - validated_data['discount']
        validated_data['total_item_amount'] = total_item_amount + (total_item_amount * Decimal(SaleDetailsProduct.TAX_RATE))
        validated_data['sale'] = sale
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Actualiza los datos del objeto
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.unit_price = validated_data.get('unit_price', instance.unit_price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.sale = validated_data.get('sale', instance.sale)
        
        # Recalcula el total_item_amount automáticamente
        total_item_amount = (instance.quantity * instance.unit_price) - instance.discount
        tax_rate = Decimal(SaleDetailsProduct.TAX_RATE)
        instance.total_item_amount = total_item_amount + (total_item_amount * tax_rate)
        
        instance.save()
        return instance
