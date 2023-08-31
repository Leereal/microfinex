from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()
class Client(TimeStampedUUIDModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    guarantor = models.ForeignKey(
        "self", 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="guaranteed_loans"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_clients"
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
