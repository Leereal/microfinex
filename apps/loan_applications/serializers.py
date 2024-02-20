from rest_framework import serializers
from .models import LoanApplication, RejectionReason

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ['id', 'client', 'amount', 'status', 'rejection_reason', 'user', 'branch']
        extra_kwargs = {'status': {'required': False, 'allow_blank': True}}

class RejectionReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RejectionReason
        fields = ['id', 'title', 'description', 'user']
