from rest_framework import serializers
from apps.loan_transactions.serializers import LoanTransactionSerializer
from apps.loans.models import Loan
from apps.loans.validation import validate_client, validate_loan_amount


class LoanSerializer(serializers.ModelSerializer):
    client_full_name = serializers.SerializerMethodField()
    branch_name = serializers.CharField(source="branch.name", read_only=True)
    loan_created_by = serializers.CharField(source="created_by.get_full_name", read_only=True)
    loan_approved_by = serializers.CharField(source="approved_by.get_full_name", read_only=True)
    transactions = LoanTransactionSerializer(many=True, source="loan_transactions", read_only=True) 
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = [
            "id", "client", "client_full_name", "branch", "branch_name",
            "created_by", "loan_created_by", "approved_by", "loan_approved_by",
            "amount", "interest_rate", "interest_amount", "currency",
            "loan_application", "disbursement_date", "start_date", "expected_repayment_date",  # Updated
            "status",'product_name', "branch_product", "group_product","transactions"
        ]
        read_only_fields = ["branch_name", "loan_created_by", "loan_approved_by", "created_by", "branch","transactions"]

    def get_product_name(self,obj):
        if obj.group_product:
            return obj.group_product.product.name
        else:
            return obj.branch_product.product.name

    def get_client_full_name(self, obj):
        return obj.client.get_full_name()

    def validate_amount(self, value):
        return validate_loan_amount(value, self.initial_data.get('client'), self.context)

    def validate(self, attrs):
        validate_client(attrs.get('client'), attrs.get('branch'))
        return attrs