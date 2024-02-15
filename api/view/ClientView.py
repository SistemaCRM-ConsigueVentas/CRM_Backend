from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.serializers.ClientSerializer import *   
from rest_framework.pagination import PageNumberPagination

class PaginationFive(PageNumberPagination):
    page_size = 5

#Listar y crear cliente
class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PaginationFive

    def get_queryset(self):
        queryset = Client.objects.all()
        search_param = self.request.query_params.get('search', None)
        if search_param:
            queryset = queryset.filter(
                name__icontains=search_param) | queryset.filter(
                lastname__icontains=search_param) | queryset.filter(
                documentNumber__icontains=search_param)
        return queryset

#Detalle, actualizar y eliminar cliente
class ClientDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        instance.state = False
        instance.save()
