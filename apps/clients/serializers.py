from datetime import timedelta
from django.utils.timezone import now
from rest_framework import serializers

from .models import Client, Contact, NextOfKin
from django_countries.serializer_fields import CountryField

class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    country_code = serializers.ReadOnlyField(source='get_country_code')
    client = serializers.PrimaryKeyRelatedField(read_only=True)    
    
    class Meta:
        model = Contact
        fields = '__all__'  # Including the 'country_code' through the source argument
        extra_kwargs = {'client': {'read_only': True}} 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['country_code'] = instance.get_country_code
        return representation


class ClientSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, required=False)  # Assuming at least one contact is required
    country = CountryField(name_only=True) 
    passport_country = CountryField(name_only=True)   
    next_of_kin = NextOfKinSerializer(required=False)
    
    class Meta:
        model = Client
        fields = '__all__'  # Or list specific fields you want to include
   
    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts', [])
        next_of_kin_data = validated_data.pop('next_of_kin', None)
        
        client = Client.objects.create(**validated_data)
        
        if next_of_kin_data:
            NextOfKin.objects.create(client=client, **next_of_kin_data)
        
        for contact_data in contacts_data:
            Contact.objects.create(client=client, **contact_data)

        # No need to call update_or_create here as the client is already created and associated correctly
        
        return client
    
    def update(self, instance, validated_data):
        # Update Next of Kin and Contacts instances together with the client
        contacts_data = validated_data.pop('contacts', [])
        next_of_kin_data = validated_data.pop('next_of_kin', None)

        # Update the Client instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update or create the Next of Kin instance
        if next_of_kin_data:
            NextOfKin.objects.update_or_create(client=instance, defaults=next_of_kin_data)

        # Keep track of contact ids to determine which to add, update, or delete
        existing_ids = set(instance.contacts.all().values_list('id', flat=True))
        incoming_ids = set(item.get('id') for item in contacts_data if item.get('id'))

        # Update or create contacts
        for contact_data in contacts_data:
            contact_id = contact_data.get('id')
            if contact_id and contact_id in existing_ids:
                # Update existing contact
                Contact.objects.filter(id=contact_id).update(**contact_data)
            elif not contact_id or contact_id not in incoming_ids:
                # Create new contact if it doesn't have an id or if the id is not recognized
                Contact.objects.create(client=instance, **contact_data)

        # Delete contacts not included in the request
        contacts_to_delete = existing_ids - incoming_ids
        if contacts_to_delete:
            instance.contacts.filter(id__in=contacts_to_delete).delete()

        return instance


    def get_age(self, obj):
        return obj.get_age()
    
    def get_country_name(self, obj):
        return obj.country.name
     
    def validate_date_of_birth(self, value):
        """
        Check that the client is at least 18 years old.
        """
        age = now().date() - value
        if age < timedelta(days=18*365.25):  # Approximation for leap years
            raise serializers.ValidationError("Client must be at least 18 years old.")
        return value
    
    def validate_passport_number(self, value):
        """
        Check that the passport number is unique if provided and not empty.
        """
        if value:  # Only proceed if value is not empty
            value = value.strip()  # Trim whitespace
            if not value:  # If it's now empty after stripping whitespace
                return None  # Treat it as None
            if Client.objects.filter(passport_number=value).exists():
                raise serializers.ValidationError("This passport number is already in use.")
        else:
            return None  # Treat empty input as None
        return value
    
    def validate_national_id(self, value):
        """
        Check that the national ID is unique if provided and not empty.
        """
        if value:  # Only proceed if value is not empty
            value = value.strip()  # Trim whitespace
            if not value:  # If it's now empty after stripping whitespace
                return None  # Treat it as None
            if Client.objects.filter(national_id=value).exists():
                raise serializers.ValidationError("This national ID is already in use.")
        else:
            return None  # Treat empty input as None
        return value
    
    def validate(self, data):
        """
        Perform custom validation to ensure either national_id or passport_number is provided.
        If passport_number is provided, ensure passport_country is also provided.
        """
        national_id = data.get('national_id', None)
        passport_number = data.get('passport_number', None)
        passport_country = data.get('passport_country', None)

        # Check if both national_id and passport_number are missing or empty
        if (not national_id or national_id == "") and (not passport_number or passport_number == ""):
            raise serializers.ValidationError("Either National ID or Passport Number must be provided.")

        # If passport_number is provided (and not just an empty string), ensure passport_country is also provided
        if passport_number and not passport_country:
            raise serializers.ValidationError("Passport Country must be provided if Passport Number is specified.")

        # Ensuring at least one contact is provided        
        contacts = data.get('contacts', [])
        if not contacts:
            raise serializers.ValidationError("At least one contact must be provided.")
        
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['age'] = instance.get_age()
        return representation



