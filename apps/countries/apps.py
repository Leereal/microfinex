from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CountriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.countries"
    verbose_name = _("Countries") #Meta option to create human readable name of the object in singular
