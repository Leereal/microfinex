from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "gender", "phone"]
    list_display_links = ["id", "user"]
    list_filter = ["id"]


admin.site.register(Profile, ProfileAdmin)