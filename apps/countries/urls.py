from django.urls import path
from .views import CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-detail'),
]
