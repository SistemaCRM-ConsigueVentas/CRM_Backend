from django.db import models
from api.model.ClientModel import Client
from api.enums.PaymentMethodEnums import PaymentMethodEnums

class Sale(models.Model):
    saleID = models.AutoField(primary_key=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=24, choices=[(e.value, e.name) for e in PaymentMethodEnums])
    status = models.CharField(max_length = 20)
    
    #clave foránea con cliente
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    
    #auditoría
    created_at = models.DateTimeField(auto_now_add=True)#Fecha de creacion
    updated_at = models.DateTimeField(auto_now=True)#Fecha de actualización

    def __str__(self):
        return self.dni