from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.model.ProviderModel import Provider
from api.serializers.ProviderSerializer import *

#Listar y crear 
class ProviderListCreate(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [IsAuthenticated]

#Detalle, actualizar y eliminar 
class ProviderDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [IsAuthenticated]