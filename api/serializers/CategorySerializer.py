from api.model.CategoryModel import Category
from api.enums.CategoryColorEnums import CategoryColorEnums
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'