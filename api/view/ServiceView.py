from rest_framework import generics, permissions, status
from api.model.ServiceModel import Service
from api.serializers.ServiceSerializer import ServiceSerializer
from rest_framework.response import Response
from rest_framework import serializers

# Listar y crear categorias
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

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