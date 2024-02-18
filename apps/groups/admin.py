from django.contrib import admin
from .models import Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'leader', 'email', 'phone', 'is_active', 'branch', 'created_by', 'status', 'created_at', 'deleted_at')
    list_filter = ('is_active', 'branch', 'created_by', 'status', 'created_at', 'deleted_at')
    search_fields = ('name', 'description', 'leader', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

admin.site.register(Group, GroupAdmin)
