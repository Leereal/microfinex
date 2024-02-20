from django.db import models
from apps.common.models import TimeStampedModel

class GroupProductCharge(TimeStampedModel):
    group_product = models.ForeignKey('GroupProduct', on_delete=models.CASCADE)
    charge = models.ForeignKey('Charge', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Group Product Charge - ID: {self.id}, Group Product: {self.group_product}"
