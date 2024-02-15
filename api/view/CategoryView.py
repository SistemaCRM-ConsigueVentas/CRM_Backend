from rest_framework import generics, permissions, status
from api.model.CategoryModel import Category
from api.serializers.CategorySerializer import CategorySerializer
from rest_framework.response import Response
from rest_framework import serializers

# Listar y crear categorias
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

# Detalles, actualizar y eliminar categoria
class CategoryDetailsUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def perform_destroy(self, instance):
        products_related = instance.product_set.count()
        if products_related > 0:
            raise serializers.ValidationError("No puedes eliminar esta categoría porque tiene productos relacionados.")

        instance.delete()
        return Response({"detail": "Categoría eliminada con éxito."}, status=status.HTTP_200_OK)