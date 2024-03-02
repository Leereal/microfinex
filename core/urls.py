from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from dj_rest_auth.views import  PasswordResetConfirmView
from apps.users.views import CustomLoginView, CustomUserDetailsView, CustomUserEditView

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
    path("api/v1/auth/login/", CustomLoginView.as_view(), name="login"),
    path("api/v1/auth/user/", CustomUserDetailsView.as_view(), name="user_details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")),   
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/auth/password/reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("api/v1/profiles/", include("apps.profiles.urls")),
    path("api/v1/branches/", include("apps.branches.urls")),
    path("api/v1/currencies/", include("apps.currencies.urls")),
    path("api/v1/branch-assets/", include("apps.branch_assets.urls")),
    path("api/v1/change-audits/", include("apps.audits.urls")),
    # path("api/v1/clients/", include("apps.clients.urls")),
    path("api/v1/users/<int:pk>/update/", CustomUserEditView.as_view(), name="update_user"),  # Endpoint for editing user data
    path("api/v1/users/", include("apps.users.urls")),
    # path("api/v1/", include("apps.loan_applications.urls")),
    path("api/v1/periods/", include("apps.periods.urls")),
    path("api/v1/products/", include("apps.products.urls")),

]

admin.site.site_header = "Microfinex Pro Admin"
admin.site.site_title = "Microfinex Pro Admin Portal"
admin.site.index_title = "Welcome to Microfinex Pro Admin Portal"
