from api.models import Product
from api.serializers.ProductSerializer import ProductSerializer
from rest_framework import generics, permissions, status, pagination
from rest_framework.response import Response
import os
from django.conf import settings

#Crear productos
class ProductRegisterView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        
    def upload_image(self):
            try:
                image = self.request.data.get('image')
                folder_path = os.path.join(settings.MEDIA_ROOT,'products')
                os.makedirs(folder_path, exist_ok=True)
                product_name = self.request.data.get('name')
                filename = product_name.replace(' ', '_').lower() + '.' + image.name.split('.')[-1]
                with open(os.path.join(folder_path, filename), 'wb') as f:
                    f.write(image.read())
                return f'products/{filename}'
            except Exception as e:
                return Response({"details": f"Error al guardar la imagen: {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def perform_create(self, serializer):
        serializer.validated_data['image'] = self.upload_image()
        
# Listar productos
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