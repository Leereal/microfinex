from django.db import models

from apps.common.models import TimeStampedModel

class Currency(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)    

    def __str__(self):
        return self.name
