from rest_framework import serializers
from api.model.UserModel import User 
from api.serializers.RoleSerializer import RoleSerializer 

# Serializer para el modelo User (para registro)
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'name', 'lastname', 'email', 'username', 'password','document_type','document_number','address','phone']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Serializer para el modelo User (para login)
class UserLoginSerializer(serializers.Serializer):
    # Especifica los campos requeridos para la autenticación
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
# Serializer para cambio de contraseña
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

# Serializer para el modelo User (List User)
class UserSerializer(serializers.ModelSerializer):   
    class Meta:
        model = User
        fields = ['id','email','name','lastname','role','username','document_type','document_number','is_staff','is_superuser','address','phone','created_at','updated_at','is_active']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user