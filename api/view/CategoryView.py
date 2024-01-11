from rest_framework import generics, permissions
from api.model.CategoryModel import Category
from api.serializers.CategorySerializer import CategorySerializer

# Listar y crear categorias
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

# Detalles, actualizar y eliminar categoria
class CategoryDetailsUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
