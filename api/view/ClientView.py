import os
from django.conf import settings
from django.core.files.storage import default_storage

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.serializers.CustomerSerializer import *   
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginationFive(PageNumberPagination):
    page_size = 5


#Listar y crear cliente
class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PaginationFive
    def upload_image(self):
        try:
            image = self.request.data.get('image')
            if image:
                folder_path = os.path.join(settings.MEDIA_ROOT, 'customers')
                os.makedirs(folder_path, exist_ok=True)
                filename = self.request.data.get('document_number') + '.' + image.name.split('.')[-1]  # Nombre de archivo personalizado
                with open(os.path.join(folder_path, filename), 'wb') as f:
                    f.write(image.read())
                return f'customers/{filename}'
            else:
                # Si no se proporciona ninguna imagen, se devuelve la ruta de la imagen predeterminada
                return f'photos/default.jpeg'
        except Exception as e:
            return Response({"details": f"Error al guardar la imagen: {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_queryset(self):
        queryset = Customer.objects.all()
        search_param = self.request.query_params.get('search', None)
        if search_param:
            queryset = queryset.filter(
                name__icontains=search_param) | queryset.filter(
                lastname__icontains=search_param) | queryset.filter(
                documentNumber__icontains=search_param)
        return queryset
    
    
#Detalle, actualizar y eliminar cliente
class ClientDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self, pk=None):
        if pk is None:  
            return self.get_serializer().Meta.model.objects.filter(active=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk , active =True).first()
        

    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            customer_serializer  = self.serializer_class(self.get_queryset(pk))
            return Response(customer_serializer.data, status=status.HTTP_200_OK)
        return Response( {'error' : 'No existe un cliente con esos datos'}, status=status.HTTP_400_BAD_REQUEST )
    
    
    def put(self, request , pk=None):
        if self.get_queryset(pk):
            customer_serializer =self.serializer_class(self.get_queryset(pk),data= request.data, partial=True)
            if customer_serializer.is_valid():
                customer_serializer.save()
                return Response(customer_serializer.data , status= status.HTTP_200_OK)
            return Response(customer_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self,request,pk=None):
        return Response(request)
    
    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

    
