from rest_framework import serializers
from apps.users.serializers import UserSerializer
from .models import BranchAssets, User
from apps.branches.serializers import BranchSerializer

class BranchSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    used_by = UserSerializer()

    # def create(self, validated_data):
    #     #I want to attach branch, user, and used_by to the validated data
    #     validated_data['branch'] = self.context['branch']
    #     validated_data['user'] = self.context['request'].user
    #     validated_data['used_by'] = self.context['used_by']
    #     return BranchAssets.objects.create(**validated_data)

    class Meta:
        model = BranchAssets
        fields = [
            "id",
            "branch",
            "item",
            "description",
            "brand",
            "color",
            "quantity",
            "user",
            "used_by",
            "purchase_date",
            "images",
        ]
     