from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notifications"
    verbose_name = _("Notifications") #Meta option to create human readable name of the object in singular
