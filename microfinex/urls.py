from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("supersecret/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("apps.users.urls")),
    path("api/v1/", include("apps.clients.urls")),
    path("api/v1/", include("apps.branches.urls")),   
    path("api/v1/", include("apps.posts.urls")),  
    path("api/v1/enquiries", include("apps.enquiries.urls")),
    path("api/v1/loans/", include("apps.loans.urls")),  
    path("api/v1/profile/", include("apps.profiles.urls")), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Microfinex Admin"
admin.site.site_title = "Microfinex Admin Portal"
admin.site.index_title = "Welcome to the Microfinex Portal"