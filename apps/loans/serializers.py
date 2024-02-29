from rest_framework import serializers

from apps.branches.models import Branch
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    # branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    # client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    client_full_name = serializers.ReadOnlyField()
    branch_name = serializers.CharField(source="branch.name", read_only=True)

    # I want to see if the property decorator makes this work
    loan_created_by = serializers.CharField(source="user.full_name", read_only=True )
    loan_approved_by = serializers.CharField(source="user.full_name", read_only=True )

    def get_client_full_name(self,obj):
        return obj.full_name()


    class Meta:
        model = Loan
        fields = ["client_full_name","branch_name","loan_created_by","loan_approved_by","amount"]

   
    # def amount_validator(self, amount):
    #     #amount must be more than branch minimum allowed
    #     if amount < 10:
    #             raise serializers.ValidationError("Amount must be greater than 100000")
        
    #     #amount must be less than branch maximum allowed
    #     #amount must be less than or equal client limit after calculating current loan plus previous loan
    
    # def branch_validator(self, branch):
    #     #branch must be active
    #     if branch.is_active == False:
    #         raise serializers.ValidationError("Branch is not active")
        
       
        
    def client_validator(self, client):         
         #client must be active
        if client.is_active == False:
            raise serializers.ValidationError("Client is not active")
        
        #Give loan only to allowed clients
        if client.status is not "Active":
             raise serializers.ValidationError("Client is not allowed to get loan at the moment")
        
        if client.branch != branch:
             raise serializers.ValidationError("Client is not from this branch")


           