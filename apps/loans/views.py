import logging

import django_filters
from django.db.models import query
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import LoanNotFound
from .models import Loan
from .pagination import LoanPagination
from .serializers import (LoanSerializer, LoanCreateSerializer,
                          LoanViewSerializer)

logger = logging.getLogger(__name__)


class LoanFilter(django_filters.FilterSet):
    loan_product = django_filters.CharFilter(
        field_name="loan_product__name", lookup_expr="icontains"
    )
    currency = django_filters.CharFilter(field_name="currency", lookup_expr="icontains")
    amount = django_filters.NumberFilter()
    amount__gt = django_filters.NumberFilter(field_name="amount", lookup_expr="gt")
    amount__lt = django_filters.NumberFilter(field_name="amount", lookup_expr="lt")

    class Meta:
        model = Loan
        fields = ["loan_product","currency","amount"]


class ListAllLoansAPIView(generics.ListAPIView):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all().order_by("-created_at")
    pagination_class = LoanPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = LoanFilter
    search_fields = []
    ordering_fields = ["created_at"]


class ListAgentsLoansAPIView(generics.ListAPIView):

    serializer_class = LoanSerializer
    pagination_class = LoanPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = LoanFilter
    search_fields = []
    ordering_fields = ["created_at"]

    def get_queryset(self):
        client = self.request.client
        queryset = Loan.objects.filter(client=client).order_by("-created_at")
        return queryset

class LoanDetailView(APIView):
    def get(self, request, id):
        try:
            loan = Loan.objects.get(id=id)
        except Loan.DoesNotExist:
            raise LoanNotFound("Loan not found")
        
        serializer = LoanSerializer(loan, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = LoanCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            # Logging the creation
            client = request.client  # Make sure this is how you get the client
            logger.info(
                f"Loan '{serializer.data.get('ref_code')}' created by {client.first_name}"
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            loan = Loan.objects.get(id=id)
        except Loan.DoesNotExist:
            raise LoanNotFound("Loan not found")

        serializer = LoanCreateSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            loan = Loan.objects.get(id=id)
        except Loan.DoesNotExist:
            raise LoanNotFound("Loan not found")

        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

