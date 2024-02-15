from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class LoanStatusConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.loan_status"
    verbose_name = _("Loan Status") #Meta option to create human readable name of the object in singular
