from api.models import Product
from api.serializers.ProductSerializer import ProductSerializer
from rest_framework import generics, permissions

# Listar y crear productos
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
# Detalle, actualizar y eliminar producto
class ProductDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
