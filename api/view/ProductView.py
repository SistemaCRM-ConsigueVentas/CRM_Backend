from api.models import Product
from api.serializers.ProductSerializer import ProductSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response

# Listar y crear productos
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        product_name = self.request.query_params.get('name')
        
        try:
            if product_name:
                queryset = Product.objects.filter(name__icontains=product_name)
                if queryset.count() == 0:
                    return Response({"message": "The searched product does not exist"}, status=404)
            else:
                queryset = Product.objects.all()

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Listar productos por id de categoría
class ProductListByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

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
