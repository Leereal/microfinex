from django.db import models

from apps.clients.models import Client
from apps.common.models import TimeStampedModel

class ClientLimit(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    max_loan = models.DecimalField(max_digits=15, decimal_places=2)
    credit_score = models.DecimalField(max_digits=15, decimal_places=2) 

    def __str__(self):
        return f"Client Limits - ID: {self.id}, Client: {self.client}"
