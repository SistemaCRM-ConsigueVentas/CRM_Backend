import os

from django.conf import settings
from django.core.files.uploadedfile import UploadedFile

from rest_framework import (generics, pagination, permissions,status)
from rest_framework.response import Response

from api.model.ServiceModel import Service
from api.serializers.ServiceSerializer import ServiceSerializer


#Crear services
class ServiceRegisterView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    def upload_image(self):
            try:
                image = self.request.data.get('image')
                folder_path = os.path.join(settings.MEDIA_ROOT,'services')
                os.makedirs(folder_path, exist_ok=True)
                product_name = self.request.data.get('name')
                filename = product_name.replace(' ', '_').lower() + '.' + image.name.split('.')[-1]
                with open(os.path.join(folder_path, filename), 'wb') as f:
                    f.write(image.read())
                return f'services/{filename}'
            except Exception as e:
                return Response({"details": f"Error al guardar la imagen: {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        image_path = self.upload_image()
        if image_path:
            serializer.validated_data['image'] = image_path
        serializer.save()
        
# Listar productos
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.PageNumberPagination

    def list(self, request, *args, **kwargs):
        product_name = self.request.query_params.get('name')
        
        try:
            if product_name:
                queryset = Service.objects.filter(name__icontains=product_name)
                if queryset.count() == 0:
                    return Response({"message": "The searched product does not exist"}, status=404)
            else:
                queryset = Service.objects.all()

            # Paginate queryset
            page = self.paginate_queryset(queryset)
            serializer = self.get_serializer(page, many=True)

            # Get total pages
            total_pages = self.paginator.page.paginator.num_pages

            return Response({
                'pagination': {
                    'total_pages': total_pages,
                    'current_page': self.paginator.page.number,
                    'count': self.paginator.page.paginator.count
                },
                'data': serializer.data
            })
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Actualizar y eliminar service
class ServiceDetailsUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        image = request.data.get('image')
        data = request.data.copy()

        # Si 'image' no es un archivo, elimina el campo 'image' de los datos de solicitud
        if image and not isinstance(image, UploadedFile):
            del data['image']
        elif 'image' in data and isinstance(data['image'], str) and data['image'].startswith("http"):
            del data['image']
        return super().update(request, data, *args, **kwargs)


    # def perform_destroy(self, instance):
    #     sale_details_service_related = instance.sale_details_service_set.count()
    #     if sale_details_service_related > 0:
    #         raise ServiceSerializer.ValidationError("No puedes eliminar esta service porque tiene detalle de ventas.")
    
    #     instance.delete()
    #     return Response({"detail": "Service eliminada con éxito."}, status=status.HTTP_200_OK)