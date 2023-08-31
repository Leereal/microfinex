from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()
    created_by = serializers.StringRelatedField() 
    
    class Meta:
        model = Loan
        exclude = []  # Include any specific fields you want to exclude
    
    def get_client(self, obj):
        return f"{obj.client.first_name} {obj.client.last_name} ({obj.client.email})"

class LoanCreateSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Loan
        exclude = ["updated_at", "pkid"]  # Exclude ref_code if you generate it automatically

class LoanViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        exclude = ["updated_at", "pkid"]  # Exclude ref_code if you generate it automatically
