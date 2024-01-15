from rest_framework import serializers
from django.contrib.auth.models import Group,Permission

class GroupPermisionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'