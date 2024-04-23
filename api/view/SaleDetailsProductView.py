from rest_framework import generics, permissions
from api.model.SaleDetailsProductModel import SaleDetailsProduct
from api.serializers.SaleDetailsProductSerializer import SaleDetailsProductSerializer

#Listar y crear
class SaleDetailsProductListCreate(generics.ListCreateAPIView):
    queryset = SaleDetailsProduct.objects.all()
    serializer_class = SaleDetailsProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        # Al crear, se calcula automáticamente el total_item_amount en el serializer
        serializer.save()

#Detalle, actualizar y eliminar
class SaleDetailsProductUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleDetailsProduct.objects.all()
    serializer_class = SaleDetailsProductSerializer
    permission_classes = [permissions.IsAuthenticated]