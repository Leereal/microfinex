from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # Currency code (e.g., USD, EUR)
    name = models.CharField(max_length=50)  # Currency name (e.g., US Dollar, Euro)
    symbol = models.CharField(max_length=5)  # Currency symbol (e.g., $, €)

    def __str__(self):
        return self.code  # Display currency code as the string representation

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
