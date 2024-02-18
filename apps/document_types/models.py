from django.db import models

from apps.common.models import TimeStampedModel

class DocumentType(TimeStampedModel):
    name = models.CharField(max_length=255)
    formats = models.JSONField(default=list)

    def __str__(self):
        return self.name
