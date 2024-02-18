from django.contrib import admin
from .models import PaymentGateway

class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'is_disbursement', 'is_repayment', 'is_active', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('type', 'is_disbursement', 'is_repayment', 'is_active', 'created_at', 'updated_at', 'deleted_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

admin.site.register(PaymentGateway, PaymentGatewayAdmin)
