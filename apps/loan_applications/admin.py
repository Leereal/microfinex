from django.contrib import admin
from .models import LoanApplication, RejectionReason

class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'amount', 'status', 'rejection_reason', 'user', 'branch', 'created_at', 'deleted_at')
    list_filter = ('status', 'user', 'branch', 'created_at', 'deleted_at')
    search_fields = ('client__name', 'amount')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

admin.site.register(LoanApplication, LoanApplicationAdmin)
admin.site.register(RejectionReason)
