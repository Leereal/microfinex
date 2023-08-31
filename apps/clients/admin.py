from django.contrib import admin
from apps.clients.models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "created_by"]
    list_filter = ["created_by"]
    search_fields = ["first_name", "last_name", "email"]

admin.site.register(Client, ClientAdmin)
