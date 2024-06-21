from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.serializers.DetailPurchaseSerializer import *   

#Listar y crear 
class DetailPurchaseListCreate(generics.ListCreateAPIView):
    queryset = DetailPurchase.objects.all()
    serializer_class = DetailPurchaseSerializer
    permission_classes = [IsAuthenticated]

#Detalle, actualizar y eliminar 
class DetailPurchaseDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailPurchase.objects.all()
    serializer_class = DetailPurchaseSerializer
    permission_classes = [IsAuthenticated]