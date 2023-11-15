import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()

class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimeStampedUserModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        editable=False
    )

    class Meta:
        abstract = True


@receiver(pre_save, sender=TimeStampedUserModel)
def set_created_by(sender, instance, **kwargs):
    from django.apps import apps
    UserModel = get_user_model()
    request = apps.get_model("django.contrib", "auth.models").get_current_request()

    if request and request.user.is_authenticated:
        instance.created_by = request.user
