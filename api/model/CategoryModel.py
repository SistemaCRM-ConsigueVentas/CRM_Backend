from django.db import models
from api.enums.CategoryColorEnums import CategoryColorEnums
from api.enums.CategoryTypeEnums import CategoryTypeEnums

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    color = models.IntegerField(choices=[(e.value, e.name) for e in CategoryColorEnums])
    type_category = models.IntegerField(choices=[(e.value, e.name) for e in CategoryTypeEnums])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
