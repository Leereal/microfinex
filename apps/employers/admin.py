from django.contrib import admin
from .models import Employer

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'contact_person', 'email', 'name', 'employment_date', 'job_title', 'created_by', 'is_active', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('client', 'employment_date', 'created_by', 'is_active', 'created_at', 'deleted_at')
    search_fields = ('contact_person', 'email', 'name', 'job_title')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

admin.site.register(Employer, EmployerAdmin)
