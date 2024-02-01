from django.db import models
from api.enums.CategoryColorEnums import CategoryColorEnums

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    color = models.IntegerField(choices=[(e.value, e.name) for e in CategoryColorEnums])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name