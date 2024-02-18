from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel

class PaymentGateway(TimeStampedModel):
    class Type(models.TextChoices):
        ONLINE = 'online', _('Online')
        OFFLINE = 'offline', _('Offline')

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=Type.choices)
    is_disbursement = models.BooleanField(default=False)
    is_repayment = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
