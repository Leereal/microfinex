from django.db import models
from apps.clients.models import Client
from apps.products.models import Product
from apps.branches.models import Branch
from django.contrib.auth import get_user_model
from apps.currencies.models import Currency
from apps.loan_applications.models import LoanApplication
from apps.loan_statuses.models import LoanStatus
from apps.common.models import TimeStampedModel

User = get_user_model()

class Loan(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='loans')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_loans')
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_loans', blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    payments = models.DecimalField(max_digits=15, decimal_places=2)
    charges = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    interest_amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    disbursement_date = models.DateTimeField()
    repayment_date = models.DateTimeField()
    status = models.ForeignKey(LoanStatus, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch_loans')

    def __str__(self):
        return f"Loan ID: {self.id}, Client: {self.client}, Product: {self.product}"

