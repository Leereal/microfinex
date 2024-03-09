from rest_framework import serializers
from django.db.models import Q
from apps.clients.models import Client
from apps.branches.models import Branch
from apps.loans.models import Loan
from apps.global_settings.models import GlobalSettings
from apps.branch_settings.models import BranchSettings

class LoanSerializer(serializers.ModelSerializer):
    client_full_name = serializers.SerializerMethodField()
    branch_name = serializers.CharField(source="branch.name", read_only=True)
    loan_created_by = serializers.CharField(source="created_by.get_full_name", read_only=True)
    loan_approved_by = serializers.CharField(source="approved_by.get_full_name", read_only=True)

    class Meta:
        model = Loan
        fields = [
            "id", "client", "client_full_name", "branch", "branch_name",
            "created_by", "loan_created_by", "approved_by", "loan_approved_by",
            "amount", "interest_rate", "interest_amount", "currency",
            "loan_application", "disbursement_date", "repayment_date",
            "status", "branch_product", "group_product"
        ]

    def get_client_full_name(self, obj):
        return obj.client.get_full_name()

    def validate_amount(self, value):
        # Fetch global settings; assuming there's only one instance
        global_settings = GlobalSettings.objects.first()
        # Determine if the loan is tied to a branch to fetch branch-specific settings
        branch_settings = BranchSettings.objects.filter(branch=self.context.get('request').user.branch).first() if self.context.get('request') else None

        min_amount = branch_settings.min_loan_amount if branch_settings else global_settings.min_loan_amount
        max_amount = branch_settings.max_loan_amount if branch_settings else global_settings.max_loan_amount

        if not (min_amount <= value <= max_amount):
            raise serializers.ValidationError(f"Amount must be between {min_amount} and {max_amount}.")

        return value

    def validate(self, attrs):
        client = attrs.get('client')
        branch = attrs.get('branch')

        # Client validations
        if not client.is_active:
            raise serializers.ValidationError({"client": "Client is not active."})

        if client.status != Client.Status.ACTIVE:
            raise serializers.ValidationError({"client": "Client is not allowed to get a loan at the moment."})

        # Ensure the client belongs to the same branch as the loan, if applicable
        if branch and client.branch != branch:
            raise serializers.ValidationError({"client": "Client is not from this branch."})

        # Additional validations can be added here as needed
        
        return attrs
