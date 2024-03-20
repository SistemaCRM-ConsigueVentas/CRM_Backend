from rest_framework import serializers
from api.model.ServiceModel import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'