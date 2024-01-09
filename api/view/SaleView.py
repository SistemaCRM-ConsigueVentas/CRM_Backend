from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.serializers.SaleSerializer import *   

#Listar y crear cliente
class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

#Detalle, actualizar y eliminar cliente
class SaleDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]