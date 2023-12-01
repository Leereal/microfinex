from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'clients', views.ClientViewSet)
router.register(r'phones', views.PhoneViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('clients/<int:id>/phones', views.PhoneViewSet.phones),
# ]
