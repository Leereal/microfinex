from rest_framework import serializers
from apps.clients.models import Client, Phone

class PhoneSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Phone
        fields = ['country_code', 'phone', 'type', 'whatsapp', 'is_primary', 'is_active'] 

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    phones = PhoneSerializer(many=True, required=False)


    class Meta:       
        model = Client
        fields = [
            'id','title', 'first_name', 'last_name', 'gender', 'email', 
            'address', 'city', 'state', 'zip_code', 'country', 'national_id', 
            'passport_number', 'passport_country', 'date_of_birth', 'guarantor', 
            'created_by', 'phones'
        ]
        depth = 1
    
    def create(self, validated_data):
        phones_data = validated_data.pop('phones', [])  # Remove phones from the validated_data
        client_instance = Client.objects.create(**validated_data)

        # Create phones related to the client
        for phone_data in phones_data:
            Phone.objects.create(client=client_instance, **phone_data)

        return client_instance