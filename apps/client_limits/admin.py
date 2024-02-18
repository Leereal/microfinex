from django.contrib import admin
from .models import ClientLimit


class ClientLimitAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'max_loan', 'credit_score', 'created_at', 'deleted_at')
    list_filter = ('client', 'created_at', 'deleted_at')
    search_fields = ('client__name',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

admin.site.register(ClientLimit, ClientLimitAdmin)
