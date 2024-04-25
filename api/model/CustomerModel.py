from django.db import models
import os
from django.conf import settings
from django.core.files.storage import default_storage
from api.enums.DocumentTypeEnums import DocumentTypeEnum
from api.enums.CustomerEnums import GenderEnum

#Modelo Clientes
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    document_type = models.IntegerField([(e.value,e.name) for e in DocumentTypeEnum])
    document_number = models.CharField(max_length=14, unique=True)
    birthdate = models.DateField()
    email = models.CharField(max_length = 30, unique=True)
    gender = models.IntegerField([(e.value,e.name) for e in GenderEnum])
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length = 40)
    postal_code = models.CharField(max_length = 10)
    province = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    image= models.ImageField (default='photos/default.jpeg',upload_to='customers', blank=True, null=True)
    #auditoría
    created_at = models.DateTimeField(auto_now_add=True)#Fecha de creacion
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk and self.image.name != 'default.jpeg':
            old_image = Customer.objects.get(pk=self.pk)
            full_image_path = os.path.join(settings.MEDIA_ROOT, 'default.jpeg')
            if old_image.image.path != self.image.path and old_image.image.path != full_image_path:
                default_storage.delete(old_image.image.path)
        super().save(*args, **kwargs)
