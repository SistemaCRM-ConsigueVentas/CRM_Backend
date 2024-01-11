from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.model.RoleModel import Role
from api.serializers.RoleSerializer import *   

#Listar y crear cliente
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

#Detalle, actualizar y eliminar Rolee
# class RoleDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer
#     permission_classes = [IsAuthenticated]