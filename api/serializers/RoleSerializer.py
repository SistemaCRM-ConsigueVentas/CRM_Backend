from rest_framework import serializers
from api.model.RoleModel import Role
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'