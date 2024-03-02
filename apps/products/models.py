from django.db import models
from apps.common.models import TimeStampedModel

class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
