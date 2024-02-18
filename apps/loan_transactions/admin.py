from django.contrib import admin
from .models import LoanTransaction

class LoanTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan', 'transaction', 'debit', 'credit', 'currency', 'created_by', 'branch', 'payment_gateway', 'status', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('transaction', 'currency', 'created_by', 'branch', 'payment_gateway', 'status', 'created_at', 'deleted_at')
    search_fields = ('loan__id', 'transaction', 'status')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

admin.site.register(LoanTransaction, LoanTransactionAdmin)
