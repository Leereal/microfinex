from rest_framework import serializers

from apps.countries.serializers import CountrySerializer
from .models import Branch

class BranchSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = Branch
        fields = [
            "id",
            "name",
            "address",
            "email",
            "phone",
            "is_active",
            "country"
        ]
