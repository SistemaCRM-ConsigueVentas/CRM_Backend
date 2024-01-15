from django.db import models
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.name