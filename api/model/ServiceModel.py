from django.db import models
from .PromotionModel import PromotionModel
from .CategoryModel import CategoryModel

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    service_time = models.DurationField()
    maintenance = models.BooleanField(default=False)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # conecciones
    promotion = models.ForeignKey(PromotionModel, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name