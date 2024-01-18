from api.model.ProductModel import Product
from api.enums.ProductStatusEnums import ProductStatusEnums
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['state'] = getattr(ProductStatusEnums, instance.state).value
        return representation

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['state'] = ProductStatusEnums(int(data['state'])).name
        return internal_value
