from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django_countries.fields import CountryField

from apps.clients.models import Client
from apps.common.models import TimeStampedUUIDModel
from apps.loan_products.models import LoanProduct
from apps.currencies.models import Currency

User = get_user_model()

class Loan(TimeStampedUUIDModel):
    ref_code = models.CharField(max_length=20, unique=True, editable=False)  # Add this field
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='loans')    
    loan_product = models.ForeignKey(LoanProduct, on_delete=models.PROTECT)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)  # Assuming you have a Currency model
    loan_term = models.PositiveIntegerField()
    application_date = models.DateField()
    status = models.CharField(max_length=50)  # You might want to use choices here
    approval_date = models.DateField(null=True, blank=True)
    disbursement_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_loans"
    )

    def __str__(self):
        return f"Loan for {self.client} - Amount: {self.loan_amount} {self.currency}"

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
    
    def save(self, *args, **kwargs):
        if not self.ref_code:
            # Generate a sequential ref_code based on the latest loan
            last_loan = Loan.objects.order_by('-pkid').first()
            if last_loan:
                last_ref_code = last_loan.ref_code
                sequence = int(last_ref_code.split('-')[-1]) + 1
            else:
                sequence = 1
            self.ref_code = f"LN-{sequence:08d}"
        super().save(*args, **kwargs)























# import random
# import string

# from autoslug import AutoSlugField
# from django.contrib.auth import get_user_model
# from django.core.validators import MinValueValidator
# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django_countries.fields import CountryField

# from apps.common.models import TimeStampedUUIDModel

# User = get_user_model()


# class LoanPublishedManager(models.Manager):
#     def get_queryset(self):
#         return (
#             super(LoanPublishedManager, self)
#             .get_queryset()
#             .filter(published_status=True)
#         )


# class Loan(TimeStampedUUIDModel):
#     class AdvertType(models.TextChoices):
#         SHORT_TERM = "Short Term Loans", _("Short Term Loans")
#         MEDIUM_TERM = "Medium Term Loans", _("Medium Term Loans")
#         LONG_TERM = "Long Term Loans", _("Long Term Loans")
      

#     class LoanType(models.TextChoices):
#         #This must be create not hard coded
#         SSB = "SSB", _("SSB")
#         STUDENT = "Student", _("Student")
#         SALARY_BASED = "Salary Based", _("Salary Based")       
#         OTHER = "Other", _("Other")

#     user = models.ForeignKey(
#         User,
#         verbose_name=_("Agent,Investor or Client"),
#         related_name="agent_client",
#         on_delete=models.DO_NOTHING,
#     )

#     title = models.CharField(verbose_name=_("Loan Title"), max_length=250)
#     slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
#     ref_code = models.CharField(
#         verbose_name=_("Loan Reference Code"),
#         max_length=255,
#         unique=True,
#         blank=True,
#     )
#     description = models.TextField(
#         verbose_name=_("Description"),
#         default="Default description...update me please....",
#     )
#     country = CountryField(
#         verbose_name=_("Country"),
#         default="ZA",
#         blank_label="(select country)",
#     )
#     city = models.CharField(verbose_name=_("City"), max_length=180, default="Pretoria")
#     postal_code = models.CharField(
#         verbose_name=_("Postal Code"), max_length=100, default="140"
#     )
#     street_address = models.CharField(
#         verbose_name=_("Street Address"), max_length=150, default="KG8 Avenue"
#     )
#     loan_number = models.IntegerField(
#         verbose_name=_("Loan Number"),
#         validators=[MinValueValidator(1)],
#         default=112,
#     )
#     amount = models.DecimalField(
#         verbose_name=_("Amount"), max_digits=8, decimal_places=2, default=0.0
#     )
#     #This must come from loan type table
#     interest = models.DecimalField(
#         verbose_name=_("Loan Interest"),
#         max_digits=6,
#         decimal_places=2,
#         default=0.15,
#         help_text="15% interest charged",
#     )
#     plot_area = models.DecimalField(
#         verbose_name=_("Plot Area(m^2)"), max_digits=8, decimal_places=2, default=0.0
#     )
#     total_floors = models.IntegerField(verbose_name=_("Number of floors"), default=0)
#     bedrooms = models.IntegerField(verbose_name=_("Bedrooms"), default=1)
#     bathrooms = models.DecimalField(
#         verbose_name=_("Bathrooms"), max_digits=4, decimal_places=2, default=1.0
#     )
#     advert_type = models.CharField(
#         verbose_name=_("Advert Type"),
#         max_length=50,
#         choices=AdvertType.choices,
#         default=AdvertType.FOR_SALE,
#     )

#     property_type = models.CharField(
#         verbose_name=_("Property Type"),
#         max_length=50,
#         choices=PropertyType.choices,
#         default=PropertyType.OTHER,
#     )

#     cover_photo = models.ImageField(
#         verbose_name=_("Main Photo"), default="/house_sample.jpg", null=True, blank=True
#     )
#     photo1 = models.ImageField(
#         default="/interior_sample.jpg",
#         null=True,
#         blank=True,
#     )
#     photo2 = models.ImageField(
#         default="/interior_sample.jpg",
#         null=True,
#         blank=True,
#     )
#     photo3 = models.ImageField(
#         default="/interior_sample.jpg",
#         null=True,
#         blank=True,
#     )
#     photo4 = models.ImageField(
#         default="/interior_sample.jpg",
#         null=True,
#         blank=True,
#     )
#     published_status = models.BooleanField(
#         verbose_name=_("Published Status"), default=False
#     )
#     views = models.IntegerField(verbose_name=_("Total Views"), default=0)

#     objects = models.Manager()
#     published = LoanPublishedManager()

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Loan"
#         verbose_name_plural = "Loans"

#     def save(self, *args, **kwargs):
#         self.title = str.title(self.title)
#         self.description = str.capitalize(self.description)
#         self.ref_code = "".join(
#             random.choices(string.ascii_uppercase + string.digits, k=10)
#         )
#         super(Loan, self).save(*args, **kwargs)

#     @loan
#     def final_property_price(self):
#         tax_percentage = self.tax
#         property_price = self.price
#         tax_amount = round(tax_percentage * property_price, 2)
#         price_after_tax = float(round(property_price + tax_amount, 2))
#         return price_after_tax


# class PropertyViews(TimeStampedUUIDModel):
#     ip = models.CharField(verbose_name=_("IP Address"), max_length=250)
#     property = models.ForeignKey(
#         Property, related_name="property_views", on_delete=models.CASCADE
#     )

#     def __str__(self):
#         return (
#             f"Total views on - {self.property.title} is - {self.property.views} view(s)"
#         )

#     class Meta:
#         verbose_name = "Total Views on Property"
#         verbose_name_plural = "Total Property Views"