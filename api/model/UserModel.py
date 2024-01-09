from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from api.model.RoleModel import Role
#Gestor de usuarios personalizado
class UserManager(BaseUserManager):
    # Método para crear un usuario regular
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El campo username es obligatorio.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Método para crear un superusuario
    def create_superuser(self, username, password=None, **extra_fields):
        # Configuración predeterminada para un superusuario
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

# Modelo de Usuario personalizado
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # id_role = models.ForeignKey(Role, null=True, blank=True)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)#Fecha de creacion
    updated_at = models.DateTimeField(auto_now=True)#Fecha de actualización

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'lastname','email']

    def __str__(self):
        return self.name

