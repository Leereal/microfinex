from django.db import models

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    min_transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
 
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"
