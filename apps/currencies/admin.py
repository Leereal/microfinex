from django.contrib import admin
from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'symbol', 'is_active', 'deleted_at')
    list_filter = ('is_active', 'deleted_at')
    search_fields = ('name', 'code', 'symbol')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

admin.site.register(Currency, CurrencyAdmin)
