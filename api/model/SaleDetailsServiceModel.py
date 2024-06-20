from decimal import Decimal
from django.db import models
from api.models import Service, Sale

class SaleDetailsService(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    # Definimos el impuesto como una constante
    TAX_RATE = Decimal('0.18')
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    total_item_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    
    # Relación muchos a uno
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='sales_details')

    def save(self, *args, **kwargs):
        # Calcula el total del ítem antes de guardar
        total_without_tax = (self.quantity * self.unit_price) - self.discount
        self.tax = total_without_tax * self.TAX_RATE
        self.total_item_amount = total_without_tax + self.tax
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SaleDetailsService - ID: {self.id}"
