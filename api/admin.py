from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from api.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Client)
admin.site.register(Sale)

admin.site.register(Permission) #Modelo para los Permisos
admin.register(Group) #Modelo para los grupos de permisos


