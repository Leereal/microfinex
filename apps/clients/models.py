from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()
class Client(TimeStampedUUIDModel):
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)        
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    national_id = models.CharField(max_length=30)
    passport_number = models.CharField(max_length=20)
    passport_country = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
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
