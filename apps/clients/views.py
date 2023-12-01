from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from .models import Client, Phone
from .serializers import ClientSerializer, PhoneSerializer

class ClientUserPermission(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.        
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.created_by == request.user

class ClientViewSet(viewsets.ModelViewSet, ClientUserPermission):
    """
    API endpoint for CRUD operations on social media platforms.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Overriding the create method to handle comments
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data)

    
    #To override the list method of the viewset
    def list(self, request):
        queryset = self.queryset
        return Response(self.serializer_class(queryset,many=True).data, status=HTTP_200_OK)
        #the queryset is filtered by the search query
        # search = request.GET.get('search') # use query like this : api/clients/?search=John
        # queryset = self.queryset
        # if search:
        #     queryset = queryset.filter(first_name__icontains=search) # use __icontains for case insensitive search
        # serializer = self.serializer_class(queryset, many=True)
        # return Response(serializer.data, status=HTTP_200_OK)


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = [IsAuthenticated]
