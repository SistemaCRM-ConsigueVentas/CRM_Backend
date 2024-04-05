from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import generics, permissions, status, pagination
from api.model.ServiceModel import Service
from api.serializers.ServiceSerializer import ServiceSerializer
from rest_framework.response import Response
from rest_framework import serializers
from PIL import Image
import io

from django.core.files.base import ContentFile
from django.core.files.images import ImageFile

import os
import imghdr
from django.conf import settings

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

        # Hacer una copia mutable de request.data
        data = request.data.copy()

        # Verificar si se proporciona una nueva imagen
        if image:
            try:
                # Abrir la imagen y convertirla en un objeto InMemoryUploadedFile
                img = Image.open(image)
                img_io = io.BytesIO()
                img.save(img_io, format='JPEG')
                img_file = InMemoryUploadedFile(img_io, None, 'foo.jpg', 'image/jpeg', img_io.getbuffer().nbytes, None)
                data['image'] = img_file
            except Exception as e:
                return Response({"details": f"Error al abrir la imagen: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return super().update(request, data, *args, **kwargs)  # Usar la copia mutable de request.data

    #def perform_destroy(self, instance):
    #    products_related = instance.product_set.count()
    #    if products_related > 0:
    #        raise serializers.ValidationError("No puedes eliminar esta service porque tiene productos relacionados.")
    #
    #    instance.delete()
    #    return Response({"detail": "Service eliminada con éxito."}, status=status.HTTP_200_OK)