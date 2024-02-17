from django.contrib import admin
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'alpha2code', 'alpha3code']
    search_fields = ['name', 'alpha2code', 'alpha3code']
    list_display_links = ['name']

admin.site.register(Country, CountryAdmin)
