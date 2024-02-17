from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedModel
from apps.countries.models import Country

class Branch(TimeStampedModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    address = models.CharField(verbose_name=_("address"), max_length=255)
    email = models.EmailField(verbose_name=_("email address"), default=None, blank=True)
    phone = PhoneNumberField(
        verbose_name=_("phone number"), max_length=30, default=None, blank=True
    )
    is_active = models.BooleanField(default=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='branches', verbose_name=_("country"))

    class Meta:
        verbose_name = _("branch")
        verbose_name_plural = _("branches")

    def __str__(self):
        return self.name
