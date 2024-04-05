from django.db import models
from api.enums.DocumentTypeEnums import DocumentTypeEnum
from api.enums.CustomerEnums import GenderEnum

#Modelo Clientes
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)

    """ document_type = models.CharField(max_length=1, choices=[(e.value, e.name) for e in DocumentTypeEnum]) """
    document_type = models.IntegerField([(e.value,e.name) for e in DocumentTypeEnum])

    document_number = models.CharField(max_length=14, unique=True)
    bitrthdate = models.DateField()
    email = models.CharField(max_length = 30)

    """ gender = models.CharField(max_length=1, choices=[(e.value, e.name) for e in GenderEnum]) """
    
    gender = models.IntegerField([(e.value,e.name) for e in GenderEnum])

    phone = models.CharField(max_length=30)
    address = models.CharField(max_length = 40)
    postal_code = models.CharField(max_length = 10)
    province = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    image= models.CharField(max_length=150)
    #auditoría
    created_at = models.DateTimeField(auto_now_add=True)#Fecha de creacion
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name