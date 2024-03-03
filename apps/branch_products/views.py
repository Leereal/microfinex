from rest_framework import generics
from .models import BranchProduct
from .serializers import BranchProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class AllBranchProductListView(generics.ListAPIView):
    queryset = BranchProduct.objects.all()
    serializer_class = BranchProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class BranchProductListCreateView(generics.ListCreateAPIView):
    serializer_class = BranchProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        """
        This view should return a list of all the branch products
        for the currently authenticated user's active branch.
        """
        user = self.request.user
        return BranchProduct.objects.filter(branch=user.active_branch)

class BranchProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BranchProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        """
        This view allows for retrieving, updating, or deleting a branch product
        based on the currently authenticated user's active branch.
        """
        user = self.request.user
        return BranchProduct.objects.filter(branch=user.active_branch)

