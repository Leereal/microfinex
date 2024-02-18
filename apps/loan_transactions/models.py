from django.db import models
from apps.common.models import TimeStampedModel
from apps.currencies.models import Currency
from apps.loans.models import Loan
from apps.payment_gateways.models import PaymentGateway
from apps.documents.models import Document
from apps.branches.models import Branch
from django.contrib.auth import get_user_model

User = get_user_model()

class LoanTransaction(TimeStampedModel):
    class TransactionType(models.TextChoices):
        DISBURSEMENT = 'disbursement', 'Disbursement'
        REPAYMENT = 'repayment', 'Repayment'
        ADMIN_FEE = 'admin_fee', 'Admin Fee'
        # Add more transaction types as needed

    class TransactionStatus(models.TextChoices):
        REVIEW = 'review', 'Review'
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        CANCELLED = 'cancelled', 'Cancelled'
        REFUND = 'refund', 'Refund'

    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    description = models.TextField()
    transaction = models.CharField(max_length=20, choices=TransactionType.choices)
    debit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    credit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    payment_gateway = models.ForeignKey(PaymentGateway, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=TransactionStatus.choices)

    def __str__(self):
        return f"Transaction ID: {self.id}, Loan: {self.loan}"

