from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel
from apps.branches.models import Branch
from apps.clients.models import Client

User = get_user_model()

class LoanApplication(TimeStampedModel):
    class Status(models.TextChoices):
        REJECTED = 'rejected', _('Rejected')
        APPROVED = 'approved', _('Approved')
        PENDING = 'pending', _('Pending')
        CANCELLED = 'cancelled', _('Cancelled')

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices)
    rejection_reason = models.ForeignKey('RejectionReason', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Loan Application {self.id} - Status: {self.status}"

class RejectionReason(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.title
