from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer

class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
