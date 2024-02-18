from django.contrib import admin
from .models import Charge

class ChargeAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'amount_type', 'charge_type', 'loan_status', 'frequency', 'mode', 'is_active', 'deleted_at']
    list_filter = ['amount_type', 'charge_type', 'loan_status', 'frequency', 'mode', 'is_active']
    search_fields = ['name', 'description']

admin.site.register(Charge, ChargeAdmin)
