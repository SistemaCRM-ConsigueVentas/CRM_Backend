from rest_framework import generics, permissions, status
from api.model.PromotionModel import Promotion
from api.serializers.PromotionSerializer import PromotionSerializer
from rest_framework.response import Response
from rest_framework import serializers

# Listar y crear categorias
class PromotionListCreate(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

# Detalles, actualizar y eliminar categoria
class PromotionDetailsUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    
    def perform_destroy(self, instance):
        services_related = instance.service_set.count()
        if services_related > 0:
            raise serializers.ValidationError("No puedes eliminar esta promotion porque tiene services relacionados.")
        instance.delete()
    
        return Response({"detail": "Promotion eliminada con éxito."}, status=status.HTTP_200_OK)