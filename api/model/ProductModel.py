from django.db import models
from api.model.CategoryModel import Category
from api.enums.ProductStatusEnums import ProductStatusEnums

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    security_stock = models.IntegerField()
    barcode = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=[(e.value, e.name) for e in ProductStatusEnums])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relación muchos a uno con categoria
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name