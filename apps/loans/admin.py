from django.contrib import admin
from .models import Loan

class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product', 'created_by', 'approved_by', 'amount', 'balance', 'payments', 'charges', 'interest_rate', 'interest_amount', 'currency', 'application', 'disbursement_date', 'repayment_date', 'status', 'branch', 'created_at', 'approved_at', 'updated_at', 'deleted_at')
    list_filter = ('client', 'product', 'created_by', 'approved_by', 'currency', 'application', 'status', 'branch', 'created_at', 'approved_at', 'deleted_at')
    search_fields = ('client__name', 'product__name', 'created_by__username', 'approved_by__username', 'currency__name', 'status__name', 'branch__name')
    readonly_fields = ('created_at', 'approved_at', 'updated_at', 'deleted_at')

admin.site.register(Loan, LoanAdmin)
