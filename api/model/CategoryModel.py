from django.db import models
from api.enums.CategoryColorEnums import CategoryColorEnums

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    color = models.CharField(max_length=20, choices=[(e.value, e.name) for e in CategoryColorEnums])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name