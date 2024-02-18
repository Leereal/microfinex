from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsUserFromBranch

from .models import Client
from .renderers import ClientJSONRenderer, ClientsJSONRenderer
from .serializers import ClientSerializer, UpdateClientSerializer

User = get_user_model()

class ClientListAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # renderer_classes = [ClientsJSONRenderer]
    permission_classes = [IsAuthenticated,IsUserFromBranch]

    def perform_create(self, serializer):
        # Capture IP address and device details before saving
        serializer.save(created_by=self.request.user)

class ClientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = UpdateClientSerializer
    renderer_classes = [ClientJSONRenderer]
    permission_classes = [IsAuthenticated,IsUserFromBranch]

    def perform_update(self, serializer):
        # Capture IP address and device details before saving
        serializer.save(request=self.request)
