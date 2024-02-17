from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _



class Country(models.Model):
    name = CountryField(
        verbose_name=_("country"), default="ZW", blank=False, null=False
    )
    alpha2code = models.CharField(unique=True, max_length=2)
    alpha3code = models.CharField(unique=True, max_length=3)

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        return f"{self.name}"
