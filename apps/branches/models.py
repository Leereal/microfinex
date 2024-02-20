from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.audits.auditing import AuditableMixin
from apps.common.models import TimeStampedModel

class Branch(AuditableMixin, TimeStampedModel):  # Inherit from AuditableMixin
    name = models.CharField(verbose_name=_("name"), max_length=255)
    address = models.TextField(verbose_name=_("address"), max_length=255, blank=True)
    email = models.EmailField(verbose_name=_("email address"), default=None, blank=True)
    phone = PhoneNumberField(
        verbose_name=_("phone number"), max_length=30, default=None, blank=True
    )
    is_active = models.BooleanField(default=True)
    country = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', 'Select Country')])


    class Meta:
        verbose_name = _("branch")
        verbose_name_plural = _("branches")

    def __str__(self):
        return self.name

    def get_audit_fields(self):
        # Override the get_audit_fields method to specify fields to audit
        return ['name', 'address', 'email', 'phone', 'is_active', 'country']
