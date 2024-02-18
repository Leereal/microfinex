from rest_framework import serializers
from .models import Client, Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['country_code', 'phone', 'type', 'is_primary', 'whatsapp']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "emails",
            "national_id",
            "nationality",
            "passport_number",
            "passport_country",
            "photo",
            "date_of_birth",
            "title",
            "gender",
            "street_number",
            "suburb",
            "zip_code",
            "city",
            "state",
            "country",
            "guarantor",
            "is_guarantor",
            "status",
            "created_by",
            "branch",
            "is_active",
            "ip_address",
            "device_details",
        ]

class UpdateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "emails",
            "national_id",
            "nationality",
            "passport_number",
            "passport_country",
            "photo",
            "date_of_birth",
            "title",
            "gender",
            "street_number",
            "suburb",
            "zip_code",
            "city",
            "state",
            "country",
            "guarantor",
            "is_guarantor",
            "status",
            "branch",
            "is_active",
            "ip_address",
            "device_details",
        ]
