from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UserBranchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user_branch"
    verbose_name = _("User Branch") #Meta option to create human readable name of the object in singular
