from api.model.CategoryModel import Category
from api.enums.CategoryColorEnums import CategoryColorEnums
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['color'] = getattr(CategoryColorEnums, instance.color).value
        return representation

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['color'] = CategoryColorEnums(int(data['color'])).name
        return internal_value