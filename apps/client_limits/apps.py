from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ClientLimitsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.client_limits"
    verbose_name = _("Client Limits") #Meta option to create human readable name of the object in singular
