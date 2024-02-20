from django.db import models
from apps.common.models import TimeStampedModel
from apps.branch_product.models import BranchProduct
from apps.charges.models import Charge

class BranchProductCharge(TimeStampedModel):
    branch_product = models.ForeignKey(BranchProduct, on_delete=models.CASCADE)
    charge = models.ForeignKey(Charge, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Branch Product Charge - ID: {self.id}, Branch Product: {self.branch_product}, Charge: {self.charge}"
