from rest_framework import serializers
from api.model.SaleModel import Sale
from .CustomerSerializer import CustomerSerializer

class SaleSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Sale
        fields = '__all__'