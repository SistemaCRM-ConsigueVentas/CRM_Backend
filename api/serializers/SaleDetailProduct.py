from rest_framework import serializers
from api.model.SaleDetailsProductModel import SaleDetailProduct


class SaleDetailProduct(serializers.ModelSerializer):
    class Meta:
        mode = SaleDetailProduct
        fields = '__all__'