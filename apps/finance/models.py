from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.branches.models import Branch

from apps.common.models import TimeStampedModel

User = get_user_model()

class Finance(TimeStampedModel):
    TYPE_CHOICES = [
        ('income', _('Income')),
        ('expense', _('Expense')),
        ('investment', _('Investment')),
        ('withdrawal', _('Withdrawal')),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    received_from = models.CharField(max_length=255)
    paid_to = models.CharField(max_length=255)
    receipt_number = models.CharField(max_length=255)
    receipt_screenshot = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    branch_id = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
