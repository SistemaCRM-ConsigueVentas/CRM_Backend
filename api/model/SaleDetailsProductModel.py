from django.db import models  
from api.model.SaleModel import Sale
from api.model.ProductModel import Product

class SaleDetailsProduct(models.Model):
    id = models.AutoField(primary_key=True)
    
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    total_item_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at=models.DateTimeField(auto_now_add=True)

    # conecciones
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name

