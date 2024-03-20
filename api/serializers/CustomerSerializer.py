from rest_framework import serializers
from api.model.CustomerModel import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'