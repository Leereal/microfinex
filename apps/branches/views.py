from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from .models import Branch
from .serializers import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on branches
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer    
    permission_classes = [IsAuthenticated, IsAdminUser]
    def list(self, request, *args, **kwargs):
        # if not request.user.is_superuser:
        #     return Response({"Forbidden": "Permission denied.You must be a superuser"}, status=HTTP_403_FORBIDDEN)
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def get_permissions(self):  
        if self.action == 'list':
            permission_classes = [DjangoModelPermissions]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]