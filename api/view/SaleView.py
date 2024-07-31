from rest_framework import generics ,status
from rest_framework.permissions import IsAuthenticated
from api.models import *
from api.serializers.SaleSerializer import *
import datetime
from django.http import JsonResponse
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncYear
from decimal import Decimal, ROUND_HALF_UP
from rest_framework.response import Response

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
        group_by = request.GET.get('type','daily')
        """ http://localhost:8000/app/sales/range-days/?start_date=2024-04-24&end_date=2024-04-30&type=yearly """

        if not start_date or not end_date:
            return JsonResponse({"error": "Please provide both start_date and end_date"}, status=400)

        try:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD"}, status=400)

        if group_by == 'daily':
            response_data = self.get_sales_by_day(start_date, end_date)
        elif group_by == 'monthly':
            response_data = self.get_sales_by_month(start_date, end_date)
        elif group_by == 'yearly':
            response_data = self.get_sales_by_year(start_date, end_date)
        else:
            return Response({"error":"Invalid type parameter. Use 'daily', 'monthly', or 'yearly'"}, status=status.HTTP_404_NOT_FOUND)

        return Response(response_data)


    def get_sales_by_day(self, start_date, end_date):
        sales = Sale.objects.filter(date__range = (start_date,end_date))
        print(sales)
        sales_by_day = sales.values('date').annotate(total_amount=Sum('total'))

        response_data = []

        for sale in sales_by_day:
            total_amount =Decimal(sale['total_amount']).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
            response_data.append(
                {
                    'name':sale['date'].strftime('%d-%m'),
                    'total':str(total_amount)
                }
            )
        return response_data
    
    
    def get_sales_by_month(self, start_date, end_date):
        sales = Sale.objects.filter(date__range=(start_date, end_date))
        sales_by_month = sales.annotate(month=TruncMonth('date')).values('month').annotate(total_amount=Sum('total')).order_by('month')

        response_data = []
        for sale in sales_by_month:
            total_amount = Decimal(sale['total_amount']).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            response_data.append({
                'month': sale['month'].strftime('%Y-%m'),
                'total': str(total_amount)
            })
        
        return response_data
    

    def get_sales_by_year(self, start_date, end_date):
        sales = Sale.objects.filter(date__range =(start_date,end_date))
        sales_by_year = sales.annotate(year=TruncYear('date')).values('year').annotate(total_amount=Sum('total')).order_by('year')
        response_data = []
        for sale in sales_by_year:
            total_amount = Decimal(sale['total_amount']).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            response_data.append({
                'year': sale['year'].strftime('%Y'),
                'total': str(total_amount)
            })
        
        return response_data
        
