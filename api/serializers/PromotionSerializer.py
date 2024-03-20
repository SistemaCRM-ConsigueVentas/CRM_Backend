from rest_framework import serializers
from api.model.PromotionModel import Promotion

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'