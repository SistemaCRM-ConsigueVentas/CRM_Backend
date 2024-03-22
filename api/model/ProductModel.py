from django.db import models
from api.model.CategoryModel import Category
from api.enums.ProductStatusEnums import ProductStatusEnums

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    barcode = models.CharField(max_length=100, unique =True)
    name = models.CharField(max_length=100, unique =True)
    description = models.TextField()
    brand = models.CharField(max_length=50)
    stock = models.IntegerField()
    stock_security = models.IntegerField()
    price = models.FloatField()
    rating = models.CharField(max_length=20)
    image = models.ImageField(upload_to="products")
    status = models.IntegerField(choices=[(e.value, e.name) for e in ProductStatusEnums])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relación muchos a uno con categoria
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name