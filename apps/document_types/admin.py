from django.contrib import admin
from .models import DocumentTypes

class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'deleted_at')
    list_filter = ('created_at', 'deleted_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

admin.site.register(DocumentTypes, DocumentTypeAdmin)
