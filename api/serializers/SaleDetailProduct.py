from rest_framework import serializers
from api.model.SaleDetailProductModel import SaleDetailProduct


class SaleDetailProduct(serializers.ModelSerializer):
    class Meta:
        mode = SaleDetailProduct
        fields = '__all__'