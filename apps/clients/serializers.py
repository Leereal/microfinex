from rest_framework import serializers
from apps.clients.models import Client

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Client
        exclude =[]
