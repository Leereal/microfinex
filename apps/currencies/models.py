from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel

class Currency(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)   

    class Meta:
        verbose_name = _("currency")
        verbose_name_plural = _("currencies") 

    def __str__(self):
        return self.name
