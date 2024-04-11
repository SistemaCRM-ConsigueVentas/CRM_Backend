from django.db import models
from api.models import Sale, Product

class SaleDetailsProduct(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    
    # impuesto
    TAX_RATE = 0.18
    tax = models.DecimalField(max_digits=5, decimal_places=2, default=TAX_RATE * 100, verbose_name='impuesto')

    total_item_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='total del ítem')

    created_at = models.DateTimeField(auto_now_add=True)
    
    # conecciones (M-1)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Calcula el total del ítem antes de guardar
        total_without_tax = (self.quantity * self.unit_price) - self.discount
        self.total_item_amount = total_without_tax + (total_without_tax * self.TAX_RATE)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SaleDetailsProduct - ID: {self.id}"