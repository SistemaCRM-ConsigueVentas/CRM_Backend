from api.models import Product
from api.serializers.ProductSerializer import ProductSerializer
from rest_framework import generics, permissions, filters
from rest_framework.response import Response

# Listar y crear productos
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ProductListByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        category_id = self.request.query_params.get('category', None)

        try:
            category_id = int(category_id)
        except (ValueError, TypeError):
            return Response({"message": "The id must be a valid integer"}, status=400)

        queryset = Product.objects.filter(category=category_id)

        if queryset.count() == 0:
            return Response({"message": "There are no products for this category"}, status=404)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# Detalle, actualizar y eliminar producto
class ProductDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
