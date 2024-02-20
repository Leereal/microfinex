from django.db import models
from apps.common.models import TimeStampedModel

class Period(TimeStampedModel):
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    duration_unit = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
