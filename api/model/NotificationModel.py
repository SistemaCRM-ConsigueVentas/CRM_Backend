import json
from django.db import models
from api.model.UserModel import User

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    date = models.DateTimeField()
    user_id =models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    list_archives = models.TextField(default="[]")

    def __str__(self):
        return f"Notification {self.id}"
    
    def add_to_archived(self, user_id):
        archived_list = json.loads(self.list_archives)
        if user_id not in archived_list:
            archived_list.append(user_id)
            self.list_archives = json.dumps(archived_list)
            self.save()

    def remove_from_archived(self, user_id):
        archived_list = json.loads(self.list_archives)
        if user_id in archived_list:
            archived_list.remove(user_id)
            self.list_archives = json.dumps(archived_list)
            self.save()

    def get_archived_users(self):
        return json.loads(self.list_archives)