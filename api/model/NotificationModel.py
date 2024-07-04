from django.db import models
from api.model.UserModel import User

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    date = models.DateField()
    user_id =models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.id