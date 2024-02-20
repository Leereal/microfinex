import re
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import LoanApplication, RejectionReason
from .serializers import LoanApplicationSerializer, RejectionReasonSerializer

User = get_user_model()

class LoanApplicationListAPIView(generics.ListCreateAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status="pending")

class LoanApplicationDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer
    permission_classes = [IsAuthenticated]

class RejectionReasonListAPIView(generics.ListCreateAPIView):
    queryset = RejectionReason.objects.all()
    serializer_class = RejectionReasonSerializer
    permission_classes = [IsAuthenticated]

class RejectionReasonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RejectionReason.objects.all()
    serializer_class = RejectionReasonSerializer
    permission_classes = [IsAuthenticated]
