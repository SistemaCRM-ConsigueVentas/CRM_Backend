from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from api.model.RoleModel import Role
from api.enums.DocumentTypeEnums import DocumentTypeEnum
from api.enums.RoleEnums import RoleEnums
#Gestor de usuarios personalizado
# class UserManager(BaseUserManager):
#     # Método para crear un usuario regular
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('El campo username es obligatorio.')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
# Modelo de Usuario personalizado
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    document_type = models.IntegerField([(e.value,e.name) for e in DocumentTypeEnum])
    document_number = models.CharField(max_length=20,unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    role = models.IntegerField([(e.value,e.name) for e in RoleEnums])

    created_at = models.DateTimeField(auto_now_add=True)#Fecha de creacion
    updated_at = models.DateTimeField(auto_now=True)#Fecha de actualización

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'lastname','email']

    def __str__(self):
        return self.name