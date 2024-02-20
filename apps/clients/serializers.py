# from os import read
# from rest_framework import serializers

# from apps.next_of_kins.serializers import NextOfKinSerializer
# from .models import Client, Contact
# from rest_framework.exceptions import ValidationError

# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = ['country_code', 'phone', 'type', 'is_primary', 'whatsapp']

# class ClientSerializer(serializers.ModelSerializer):
#     loans = serializers.StringRelatedField(many=True, read_only=True)
#     loan_applications = serializers.StringRelatedField(many=True, read_only=True)
#     contacts = ContactSerializer(many=True)
#     next_of_kin = NextOfKinSerializer(required=False)
    
#     class Meta:
#         model = Client
#         fields = [
#             "id",
#             "first_name",
#             "last_name",
#             "emails",
#             "national_id",
#             "nationality",
#             "passport_number",
#             "passport_country",
#             "photo",
#             "date_of_birth",
#             "title",
#             "gender",
#             "street_number",
#             "suburb",
#             "zip_code",
#             "city",
#             "state",
#             "country",
#             "guarantor",
#             "is_guarantor",
#             "status",
#             "created_by",
#             "branch",
#             "is_active",
#             "ip_address",
#             "device_details",
#             "loans",
#             "loan_applications",
#             "contacts",
#             "next_of_kin",
#         ]

#     def create(self, validated_data):
#         contacts_data = validated_data.pop('contacts')
#         next_of_kin_data = validated_data.pop('next_of_kin',None)
#         client = Client.objects.create(**validated_data)
        
#         #Save contacts and atleast one contact is required
#         if contacts_data:
#             for contact_data in contacts_data:
#                 Contact.objects.create(client=client, **contact_data)
#         else:
#             raise ValidationError("Contacts data is required.")
        
#         if next_of_kin_data:
#             NextOfKinSerializer.create(NextOfKinSerializer(), next_of_kin_data, client)

#         return client

# class UpdateClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = [
#             "emails",
#             "national_id",
#             "nationality",
#             "passport_number",
#             "passport_country",
#             "photo",
#             "date_of_birth",
#             "title",
#             "gender",
#             "street_number",
#             "suburb",
#             "zip_code",
#             "city",
#             "state",
#             "country",
#             "guarantor",
#             "is_guarantor",
#             "status",
#             "branch",
#             "is_active",
#             "ip_address",
#             "device_details",
#         ]
    
#     # def update(self, instance, validated_data):
#     #     request = self.context.get('request')

#     #     # Check if the request was performed by user or contains user.
#     #     if not request or not request.user:
#     #         # Raise error or if use default user null / something
#     #         raise ValidationError("Request or user not found in context.")
#     #     print("User : ",request.user)
#     #     #Add the user to the validated data
#     #     validated_data['created_by'] = request.user
        

#     #     return super().update(instance, validated_data)
