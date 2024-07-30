from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.serializers.SaleSerializer import *
import datetime
from django.http import JsonResponse
from django.db.models import Sum
from decimal import Decimal, ROUND_HALF_UP

#Listar y crear cliente
class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

#Detalle, actualizar y eliminar cliente
class SaleDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

# Buscar ventas por rango de fechas
class SalesInRangeView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if not start_date or not end_date:
            return JsonResponse({"error": "Please provide both start_date and end_date"}, status=400)

        try:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD"}, status=400)

        sales = Sale.objects.filter(date__range=(start_date, end_date))

        # Agrupar ventas por día y calcular el total por día
        sales_by_day = sales.values('date').annotate(total_amount=Sum('total'))

        # Crear el arreglo de respuesta
        response_data = []
        for sale in sales_by_day:
            total_amount = Decimal(sale['total_amount']).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            response_data.append({
                'name': sale['date'].strftime('%d-%m'),
                'total': str(total_amount)
            })

        return JsonResponse(response_data, safe=False)
