from rest_framework import serializers
from .models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    branch_name = serializers.ReadOnlyField(source='branch.name')
    created_by_full_name = serializers.ReadOnlyField(source='created_by.get_full_name')

    class Meta:
        model = Group
        fields = [
            'id', 
            'name', 
            'description', 
            'leader', 
            'email', 
            'phone', 
            'is_active', 
            'branch', 
            'branch_name', 
            'created_by', 
            'created_by_full_name', 
            'status',
            'created_at', 
            'last_modified'
        ]
