from django.db import models
from api.enums.DocumentTypeEnums import DocumentTypeEnum

class Client(models.Model):
    clientID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    documentType = models.CharField(max_length=1, choices=[(e.value, e.name) for e in DocumentTypeEnum])
    documentNumber = models.CharField(max_length=14, unique=True)
    email = models.CharField(max_length = 30)
    cellNumber = models.CharField(max_length = 12)
    address = models.CharField(max_length = 40)
    
    #auditoría
    created_at = models.DateTimeField(auto_now_add=True)#Fecha de creacion

    def __str__(self):
        return self.name