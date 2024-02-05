from api.model.CategoryModel import Category
from api.enums.CategoryColorEnums import CategoryColorEnums
from rest_framework import serializers
from api.model.ProductModel import Product

class CategorySerializer(serializers.ModelSerializer):
    products_related = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_products_related(self, category):
        return Product.objects.filter(category=category).count()