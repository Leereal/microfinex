from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Microfinex Pro API",
        default_version='v1',
        description="The api for Microfinex Pro",
        contact=openapi.Contact(email="leereal08@ymail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Microfinex Pro Admin"
admin.site.site_title = "Microfinex Pro Admin Portal"
admin.site.index_title = "Welcome to Microfinex Pro Admin Portal"
