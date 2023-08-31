from django.db import models

class LoanProduct(models.Model):
    name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    max_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    min_loan_term = models.PositiveIntegerField()
    max_loan_term = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Loan Product"
        verbose_name_plural = "Loan Products"
