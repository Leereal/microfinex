from django.db import models

class LoanStatus(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    allow_auto_calculations = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)    

    def __str__(self):
        return self.name
