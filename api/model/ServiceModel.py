from django.db import models
from api.model.PromotionModel import Promotion
from api.model.CategoryModel import Category

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    service_time = models.DurationField()
    maintenance = models.BooleanField(default=False)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    img_url = models.CharField(max_length=150, null = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # conecciones
    promotion = models.ForeignKey(Promotion, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name