from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import NextOfKin

class NextOfKinAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'relationship', 'is_active','client']
    list_display_links = ["id","client"]
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'relationship']
    list_filter = ['is_active']

    def email(self, obj):
        return obj.email if obj.email else None
    email.short_description = _('Email')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Check if the client has any next of kin
        if not obj.client.next_of_kin.exists():
            raise ValidationError(_('At least one next of kin must be provided for the client.'))

admin.site.register(NextOfKin, NextOfKinAdmin)
