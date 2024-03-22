from api.models import Product
from api.serializers.ProductSerializer import ProductSerializer
from rest_framework import generics, permissions, status, pagination
from rest_framework.response import Response

# Listar y crear productos


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.PageNumberPagination

    def list(self, request, *args, **kwargs):
        product_name = self.request.query_params.get('name')
        
        try:
            if product_name:
                queryset = Product.objects.filter(name__icontains=product_name)
                if queryset.count() == 0:
                    return Response({"message": "The searched product does not exist"}, status=404)
            else:
                queryset = Product.objects.all()

            # Paginate queryset
            page = self.paginate_queryset(queryset)
            serializer = self.get_serializer(page, many=True)

            # Get total pages
            total_pages = self.paginator.page.paginator.num_pages

            return Response({
                'pagination': {
                    'total_pages': total_pages,
                    'current_page': self.paginator.page.number,
                    'count': self.paginator.page.paginator.count
                },
                'data': serializer.data
            })
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Listar productos por id de categoría
class ProductListByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        category_ids = self.request.query_params.getlist('category', None)

        if not category_ids:
            return Response({"message": "At least one category ID is required"}, status=400)

        queryset = Product.objects.filter(category__in=category_ids)

        if not queryset.exists():
            return Response({"message": "There are no products for these categories"}, status=404)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
# Detalle, actualizar y eliminar producto
class ProductDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
