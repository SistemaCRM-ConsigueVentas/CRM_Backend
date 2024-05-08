from django.db import models
from api.model.CustomerModel import Customer
from api.model.UserModel import User
from api.enums.PaymentMethodEnums import PaymentMethodEnums
from api.enums.SaleStatusEnums import SaleStatusEnums

class Sale(models.Model):
    saleID = models.AutoField(primary_key=True)
    date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paymentType = models.CharField(max_length=1, choices=[(e.value, e.name) for e in PaymentMethodEnums])
    saleStatus = models.CharField(max_length=1, choices=[(e.value, e.name) for e in SaleStatusEnums])
    note = models.TextField(null=True, blank=True)
    
    #clave foránea con cliente
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    #auditoría
    created_at = models.DateTimeField(auto_now_add=True)#Fecha de creacion
    updated_at = models.DateTimeField(auto_now=True)#Fecha de actualización

    def __str__(self):
        return str(self.saleID)