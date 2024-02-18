from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserBranchSerializer, UserSerializer


class CustomUserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()

class CustomUserEditView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Restrict access to admin users

    def get_object(self):
        pk = self.kwargs.get('pk')
        return User.objects.get(pk=pk)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Updating user's branches if provided in the request
        branches_data = request.data.get('branches')    
        print("Branches Data : ", branches_data)   
        if branches_data:
            user_branches = instance.user_branches.all()
            print("User Branches : ", user_branches)
            user_branch_serializer = UserBranchSerializer(user_branches, data=branches_data, many=True)
            print("User Branch Serializer : ", user_branch_serializer)
            if user_branch_serializer.is_valid():
                print("User Branch Serializer Valid : ", user_branch_serializer.is_valid)
                user_branch_serializer.save()
                return Response(user_branch_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(user_branch_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # No branches data provided, return error
            return Response({"detail": "No branches data provided"}, status=status.HTTP_400_BAD_REQUEST)