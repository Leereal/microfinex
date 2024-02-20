from django.contrib import admin
from .models import GroupProductCharge

@admin.register(GroupProductCharge)
class GroupProductChargeAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_product', 'charge', 'is_active', 'deleted_at')
    list_filter = ('group_product', 'charge', 'is_active', 'deleted_at')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
