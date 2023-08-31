from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListAllLoansAPIView.as_view(), name="all-loans"),
    path("agents", views.ListAgentsLoansAPIView.as_view(), name="agent-loans"),
    path("create", views.LoanDetailView.as_view(), name="loan-create"),
    path("<int:id>",views.LoanDetailView.as_view(), name="loan-details"),    
]