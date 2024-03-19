from django.db import models

class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    ending_date = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
