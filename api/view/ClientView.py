from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.serializers.CustomerSerializer import *   
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import os
from django.conf import settings


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
    
    def perform_destroy(self, instance):
        instance.state = False
        instance.save()
