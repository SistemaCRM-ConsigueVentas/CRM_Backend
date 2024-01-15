from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from api.serializers.PermissionsSerializer import GroupPermisionsSerializer

class GroupCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GroupPermisionsSerializer

    def create(self, request, *args, **kwargs):
        group_name = request.data.get("name")

        try:
            # Intenta obtener el grupo por su nombre
            Group.objects.get(name=group_name)

            # Si el grupo existe, devuelve una respuesta indicando que ya existe
            return Response({"message": "El grupo ya existe"}, status=status.HTTP_400_BAD_REQUEST)

        except Group.DoesNotExist:
            # Si el grupo no existe, créalo y devuelve una respuesta exitosa
            Group.objects.create(name=group_name)
            return Response({"message": "Grupo creado exitosamente"}, status=status.HTTP_201_CREATED)
    
class GroupListView(generics.ListAPIView):
    serializer_class = GroupPermisionsSerializer
    queryset = Group.objects.all()
