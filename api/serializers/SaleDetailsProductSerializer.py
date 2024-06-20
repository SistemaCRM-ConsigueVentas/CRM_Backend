from rest_framework import serializers
from api.models import SaleDetailsProduct, Sale, Product
from .ProductSerializer import ProductSerializer
from .SaleSerializer import SaleSerializer

class SaleDetailsProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),source='product', write_only=True)
    sale_obj = SaleSerializer(source='sale', read_only=True)
    sale = serializers.PrimaryKeyRelatedField(queryset=Sale.objects.all(), write_only=True)
    
    tax = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    total_item_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = SaleDetailsProduct
        fields = ['id', 'quantity', 'unit_price', 'discount', 'tax', 'total_item_amount', 'created_at', 'sale_obj','sale', 'product', 'product_id']


    def get_sale_data(self, obj):
        sale = obj.sale 
        sale_serializer = SaleSerializer(sale)
        return sale_serializer.data

    def create(self, validated_data):
        instance = SaleDetailsProduct(**validated_data)
        total_without_tax = (instance.quantity * instance.unit_price) - instance.discount
        instance.tax = total_without_tax * SaleDetailsProduct.TAX_RATE
        instance.total_item_amount = total_without_tax + instance.tax
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.unit_price = validated_data.get('unit_price', instance.unit_price)
        instance.discount = validated_data.get('discount', instance.discount)

        # Recalculamos total_item_amount y tax automáticamente
        total_without_tax = (instance.quantity * instance.unit_price) - instance.discount
        instance.tax = total_without_tax * SaleDetailsProduct.TAX_RATE
        instance.total_item_amount = total_without_tax + instance.tax

        # Actualizamos Sale si se proporciona
        sale_data = validated_data.pop('sale', None)
        if sale_data:
            instance.sale = sale_data

        # Actualizamos Product si se proporciona 
        product_data = validated_data.pop('product', None)
        if product_data:
            instance.product = product_data

        instance.save()
        return instance
