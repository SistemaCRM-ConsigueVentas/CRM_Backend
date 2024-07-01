from django.db import models
from api.models import Purchase

class DetailPurchase(models.Model):
    id = models.AutoField(primary_key=True)
    date_purchase = models.DateField()
    item = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super(DetailPurchase, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.item