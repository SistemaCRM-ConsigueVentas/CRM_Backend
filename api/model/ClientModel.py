from django.db import models

class Client(models.Model):
    clientID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    dni = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 12)
    address = models.CharField(max_length = 40)

    def __str__(self):
        return self.name