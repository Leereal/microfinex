from dataclasses import field, fields
from rest_framework import serializers
from .models import BranchProduct

class BranchProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchProduct
        fields = [
            "id",
            "branch",
            "product",
            "interest",
            "max_amount",
            "min_amount",
            "period",
            "min_period",
            "max_period",
            "is_active",
            "created_by",
        ]
        #You can specify the fields you don't want to be added or updated it's values
        # read_only_fields = ['is_active']

