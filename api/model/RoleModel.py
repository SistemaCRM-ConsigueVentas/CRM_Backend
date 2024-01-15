from django.db import models
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)#Fecha de creacion
    updated_at = models.DateTimeField(auto_now=True)#Fecha de actualización

    def __str__(self):
        return self.name