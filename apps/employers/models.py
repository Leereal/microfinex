from django.db import models
from django.contrib.auth import get_user_model
from apps.clients.models import Client
from apps.common.models import TimeStampedModel

User = get_user_model()

class Employer(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.JSONField(default=list)
    name = models.CharField(max_length=255)
    address = models.TextField()
    employment_date = models.DateField()
    job_title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
