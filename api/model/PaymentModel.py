from django.db import models

class Payment(models.Model):
    id = models.AutoField(primary_key=True)    
    date_payment = models.DateField()
    date_limit = models.DateField()
    
    payment_method = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cancelled_total = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.CharField(max_length=50)
    
    def __str__(self):
        return self.id