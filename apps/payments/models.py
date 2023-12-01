from django.db import models
from apps.common.models import TimeStampedUserModel  # Assuming you have a TimeStampedUUIDModel
from apps.loans.models import Loan 
from apps.payment_methods.models import PaymentMethod

class Payment(TimeStampedUserModel):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    receipt_number = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Payment for Loan {self.loan} - Amount: {self.amount}, Date: {self.date}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
