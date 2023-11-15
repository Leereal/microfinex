from django.contrib import admin
from apps.clients.models import Client, Phone

class PhoneInline(admin.TabularInline): #This is so that we add Phone together with Client
    model = Phone
    extra = 1 # how many rows to show

class ClientAdmin(admin.ModelAdmin):
    list_display = ["id","first_name", "last_name", "email", "created_by","full_address"]
    list_filter = ["created_by","gender","country"]
    search_fields = ["first_name", "last_name", "email"]
    inlines = [PhoneInline] #This is so that we add Phone together with Client

admin.site.register(Client, ClientAdmin)
