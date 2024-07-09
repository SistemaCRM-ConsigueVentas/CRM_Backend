from django.db import models
from api.models import Provider
from api.model.DetailPurchaseModel import DetailPurchase

class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    date_purchase = models.DateField()
    number_bill = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    detailpurchase = models.ForeignKey(DetailPurchase, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)