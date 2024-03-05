from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.utils.translation import gettext_lazy as _
from .models import Client, Contact, NextOfKin

# class NextOfKinInlineFormSet(BaseInlineFormSet):
#     def save_new(self, form, commit=True):
#         # Custom logic to ensure one-to-one relationship is maintained
#         return super().save_new(form, commit=commit)

#     def save_existing(self, form, instance, commit=True):
#         # Custom logic for updating the existing instance
#         return super().save_existing(form, instance, commit=commit)

# class NextOfKinInline(admin.StackedInline):
#     model = NextOfKin
#     formset = NextOfKinInlineFormSet
#     can_delete = False  # Optional: if you want to prevent deletion of NextOfKin from Client admin
#     verbose_name_plural = 'Next of Kin'  # Adjust the text to fit your needs


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1  # Number of empty forms to display
    fields = ('type', 'phone', 'is_primary', 'is_active', 'whatsapp')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('get_full_name','first_name', 'last_name', 'national_id', 'nationality', 'status', 'get_age')
    list_filter = ('status', 'nationality', 'gender', 'branch')
    search_fields = ('first_name', 'last_name', 'national_id', 'emails', 'passport_number')
    inlines = [ContactInline]
    fieldsets = (
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'emails', 'national_id', 'nationality', 'passport_number', 'passport_country', 'photo', 'date_of_birth', 'title', 'gender')}),
        (_('Address'), {'fields': ('street_number', 'suburb', 'zip_code', 'city', 'state', 'country')}),
        (_('Status'), {'fields': ('status', 'is_active', 'guarantor', 'is_guarantor')}),
        (_('Branch Info'), {'fields': ('branch', 'created_by')}),
        (_('Technical Details'), {'fields': ('ip_address', 'device_details')}),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(ClientAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['created_by'].initial = request.user.id
        return form

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('client', 'phone', 'type', 'is_primary', 'is_active', 'whatsapp','get_country_code')
    list_filter = ('type', 'is_active', 'whatsapp')
    search_fields = ('client__first_name', 'client__last_name', 'phone')

    def get_country_code(self, obj):
        return obj.get_country_code
    get_country_code.short_description = _('Country Code')


