from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import TimeStampedUserModel

User = get_user_model()
class Client(TimeStampedUserModel):
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
    national_id = models.CharField(max_length=30, unique=True, blank=True, null=True)
    passport_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    passport_country = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    guarantor = models.ForeignKey(
        "self", 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
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
    
    def full_address(self):
        return f"{self.address}, {self.city}, {self.zip_code}, {self.state}, {self.country}"
    #There is no need of doing the following. It's for educational purpose only
    # def save(self, *args, **kwargs):
    #     if(self.last_name == "Mutabvugri"):
    #         return #Do not save if last name is Mutabvuri
    #     else:
    #         super().save(*args, **kwargs) # Call the "real" save() method.

    #This is not included as part of the fields in the database
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["last_name", "first_name"]

class Phone(TimeStampedUserModel):   
    client = models.ForeignKey(
        Client, #This is the same as putting  Client without quotes but we have to put it in quotes if it is not defined yet
        on_delete=models.CASCADE,
        related_name="phones"
    )
    country_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    whatsapp = models.BooleanField(default=False)
    is_primary = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.type} Phone - {self.phone}"
    def full_phone(self):
        return f"({self.country_code}) {self.phone}"
    
    # def save(self, *args, **kwargs):
    #     if(self.is_primary == True): #all primary numbers must be active
    #         self.is_active = True
    #     super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"     
    
class Document(TimeStampedUserModel):
    FILE_TYPES = (
        ("ID", "ID"),
        ("PASSPORT", "PASSPORT"),
        ("DRIVERS_LICENSE", "DRIVERS_LICENSE"),        
        ("OTHER", "OTHER"),
    )
    client = models.ForeignKey(
        Client, 
        on_delete=models.CASCADE,
        related_name="documents"
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100,choices=FILE_TYPES, default="OTHER")
    file = models.FileField(upload_to="documents/%Y/%m/%d/",unique=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"



