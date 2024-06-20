from django.db import models

class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=255)
    ruc = models.IntegerField()
    person_contact = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    address = models.TextField()
    note = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name