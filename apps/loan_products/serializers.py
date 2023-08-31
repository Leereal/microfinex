from rest_framework import serializers

from .models import LoanProduct


class LoanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProduct
        fields = "__all__"