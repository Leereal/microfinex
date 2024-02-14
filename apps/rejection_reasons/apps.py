from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class RejectionReasonsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.rejection_reasons"
    verbose_name = _("Rejection Reasons") #Meta option to create human readable name of the object in singular
