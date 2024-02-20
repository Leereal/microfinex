from django.db import models
from apps.common.models import TimeStampedModel
from .models import Branch, Product
from django.contrib.auth import get_user_model
from apps.periods.models import Period

User = get_user_model()

class BranchProduct(TimeStampedModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    interest = models.DecimalField(max_digits=15, decimal_places=2)
    max_amount = models.DecimalField(max_digits=15, decimal_places=2)
    min_amount = models.DecimalField(max_digits=15, decimal_places=2)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    min_period = models.IntegerField()
    max_period = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Branch: {self.branch}, Product: {self.product}"
