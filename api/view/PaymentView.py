from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.model.PaymentModel import *
from api.serializers.PaymentSerializer import *   

#Listar y crear 
class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

#Detalle, actualizar y eliminar 
class PaymentDetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]