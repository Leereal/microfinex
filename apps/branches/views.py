from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response

from .models import Branch
from .serializers import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on branches
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer    
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    def list(self, request):
        print("Therer ",IsAuthenticated)
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)