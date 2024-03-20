from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from api.model.RoleModel import Role
from api.enums.DocumentTypeEnums import DocumentTypeEnum
from api.enums.RoleEnums import RoleEnums
import os

def photo_path(instance, filename):
    # Obtén el nombre de usuario del objeto de usuario
    dni = instance.dni
    # Obtén la extensión del archivo
    _, ext = os.path.splitext(filename)
    # Construye el nombre del archivo de la foto usando el dni del usuario y la extensión
    return os.path.join('photos', f'{dni}{ext}')

#Modelo Usuarios
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    document_type = models.IntegerField([(e.value,e.name) for e in DocumentTypeEnum])
    document_number = models.CharField(max_length=20,unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    image= models.ImageField(upload_to=photo_path)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.IntegerField([(e.value,e.name) for e in RoleEnums])

    created_at = models.DateTimeField(auto_now_add=True)#Fecha de creacion
    updated_at = models.DateTimeField(auto_now=True)#Fecha de actualización

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'lastname']

    def __str__(self):
        return self.name
    
    
