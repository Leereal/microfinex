from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'loan', 'name', 'file_path', 'document_type', 'uploaded_by', 'branch', 'created_at', 'deleted_at')
    list_filter = ('document_type', 'uploaded_by', 'branch', 'created_at', 'deleted_at')
    search_fields = ('name', 'file_path')
    readonly_fields = ('created_at', 'deleted_at')
