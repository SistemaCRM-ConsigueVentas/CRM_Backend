from rest_framework import generics, permissions, status
from api.model.ServiceModel import Service
from api.serializers.ServiceSerializer import ServiceSerializer
from rest_framework.response import Response
from rest_framework import serializers

import os
import imghdr
from django.conf import settings

# Listar y crear categorias
class ServiceListCreate(generics.ListCreateAPIView):
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


# Detalles, actualizar y eliminar categoria
class ServiceDetailsUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    #def perform_destroy(self, instance):
    #    products_related = instance.product_set.count()
    #    if products_related > 0:
    #        raise serializers.ValidationError("No puedes eliminar esta service porque tiene productos relacionados.")
#
    #    instance.delete()
    #    return Response({"detail": "Service eliminada con éxito."}, status=status.HTTP_200_OK)