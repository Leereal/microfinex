from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class NextOfKinsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.next_of_kins"
    verbose_name = _("Next Of Kins") #Meta option to create human readable name of the object in singular

    def ready(self):
        from apps.next_of_kins import signals