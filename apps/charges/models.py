

from django.db import models
from django.utils.translation import gettext_lazy as _

class Charge(models.Model):
    AMOUNT_TYPE_CHOICES = [
        ('fixed', _('Fixed')),
        ('percentage', _('Percentage')),
    ]
    CHARGE_TYPE_CHOICES = [
        ('credit', _('Credit')),
        ('debit', _('Debit')),
    ]
    FREQUENCY_CHOICES = [
        ('one-time', _('One-time')),
        ('recurring', _('Recurring')),
    ]
    MODE_CHOICES = [
        ('manual', _('Manual')),
        ('auto', _('Auto')),
    ]
    APPLICATION_CHOICES = [
        ('principal', _('Principal')),
        ('balance', _('Balance')),
        ('other', _('Other')),
    ]

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)    
    amount_type = models.CharField(max_length=20, choices=AMOUNT_TYPE_CHOICES)   
    charge_type = models.CharField(max_length=20, choices=CHARGE_TYPE_CHOICES)
    charge_application = models.CharField(max_length=20, choices=APPLICATION_CHOICES, default='principal')  # New field
    loan_status = models.ForeignKey('LoanStatus', on_delete=models.CASCADE)   
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)    
    mode = models.CharField(max_length=20, choices=MODE_CHOICES)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
