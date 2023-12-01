from django.db import models
from django.utils.translation import gettext_lazy as _

class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Branch")
        verbose_name_plural = _("Branches")
