from django.contrib import admin
from .models import Loan

class LoanAdmin(admin.ModelAdmin):
    list_display = ["client", "loan_product", "loan_amount", "status",'created_by']
    list_filter = ["status", "loan_product"]
    search_fields = ["client__email", "client__first_name", "client__last_name"]  # Add more search fields if needed

admin.site.register(Loan, LoanAdmin)
