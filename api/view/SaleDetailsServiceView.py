from rest_framework import generics, permissions
from api.model.SaleDetailsServiceModel import SaleDetailsService
from api.serializers.SaleDetailsServiceSerializer import SaleDetailsServiceSerializer

#Listar y crear
class SaleDetailsServiceListCreate(generics.ListCreateAPIView):
    queryset = SaleDetailsService.objects.all()
    serializer_class = SaleDetailsServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        # Al crear, se calcula automáticamente el total_item_amount en el serializer
        serializer.save()

#Detalle, actualizar y eliminar
class SaleDetailsServiceUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleDetailsService.objects.all()
    serializer_class = SaleDetailsServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

