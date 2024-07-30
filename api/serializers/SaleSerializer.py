from decimal import Decimal
from django.db.models import Sum
from rest_framework import serializers
from api.model.CustomerModel import Customer
from api.models import Sale
from api.models import SaleDetailsService, SaleDetailsProduct
from api.serializers.CustomerSerializer import CustomerSerializer

class SaleSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', write_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), read_only=True)

    class Meta:
        model = Sale
        fields = '__all__'
        read_only_fields = ('total',)

    def create(self, validated_data):
        customer = validated_data.pop('customer')
        user = validated_data.pop('user')
        # aqui la solucion, la instancia Sale definida con campo relacional
        sale = Sale.objects.create(customer=customer, user=user, **validated_data)
        self._update_total(sale)
        return sale

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.paymentType = validated_data.get('paymentType', instance.paymentType)
        instance.saleStatus = validated_data.get('saleStatus', instance.saleStatus)
        instance.note = validated_data.get('note', instance.note)
        instance.customer = validated_data.get('customer', instance.customer)
        instance.user = validated_data.get('user', instance.user)
        instance.save()

        self._update_total(instance)
        return instance

    def _update_total(self, sale):
        total_sale_details_service = SaleDetailsService.objects.filter(sale=sale).aggregate(total_amount=Sum('total_item_amount'))['total_amount'] or Decimal('0.00')
        total_sale_details_product = SaleDetailsProduct.objects.filter(sale=sale).aggregate(total_amount=Sum('total_item_amount'))['total_amount'] or Decimal('0.00')

        sale.total = total_sale_details_service + total_sale_details_product
        sale.save()