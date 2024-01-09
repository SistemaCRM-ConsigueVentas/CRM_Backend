from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.serializers.ClientSerializer import *   

#Listar y crear cliente
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

#Detalle, actualizar y eliminar cliente
class ClientDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]