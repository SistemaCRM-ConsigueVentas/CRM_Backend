from decimal import Decimal
from django.db import models
from django.db.models import Sum
from api.models import Customer, User
from api.enums.PaymentMethodEnums import PaymentMethodEnums
from api.enums.SaleStatusEnums import SaleStatusEnums

class Sale(models.Model):
    saleID = models.AutoField(primary_key=True)
    date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)
    paymentType = models.CharField(max_length=1, choices=[(e.value, e.name) for e in PaymentMethodEnums])
    saleStatus = models.CharField(max_length=1, choices=[(e.value, e.name) for e in SaleStatusEnums])
    note = models.TextField(null=True, blank=True)
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        total_sale_details_service = self.saledetailsservice_set.aggregate(total_amount=Sum('total_item_amount'))['total_amount'] or Decimal('0.00')
        total_sale_details_product = self.saledetailsproduct_set.aggregate(total_amount=Sum('total_item_amount'))['total_amount'] or Decimal('0.00')

        return total_sale_details_service + total_sale_details_product

    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.saleID)