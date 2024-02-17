from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField

from apps.common.models import TimeStampedModel
from apps.clients.models import Client

User = get_user_model()

class NextOfKin(TimeStampedModel):
    client = models.ForeignKey(Client, verbose_name=_('Client'), related_name='next_of_kin', on_delete=models.CASCADE)
    first_name = models.CharField(_('First Name'), max_length=50)
    last_name = models.CharField(_('Last Name'), max_length=50)
    email = models.EmailField(_('Email'),blank=True,null=True)
    phone = PhoneNumberField(_('Phone Number'), blank=True,null=True)
    relationship = models.CharField(_('Relationship'), max_length=255)
    address = models.TextField(_('Address'))
    created_by = models.ForeignKey(User, verbose_name=_('Created By'), on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(_('Is Active'), default=True)

    class Meta:
        verbose_name = _('Next of Kin')
        verbose_name_plural = _('Next of Kin')

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Relationship: {self.relationship})"
