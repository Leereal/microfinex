from django.urls import path
from .views import LoanApplicationListAPIView, LoanApplicationDetailAPIView, RejectionReasonListAPIView, RejectionReasonDetailAPIView

urlpatterns = [
    path("loan-applications/", LoanApplicationListAPIView.as_view(), name="loan-application-list"),
    path("loan-applications/<int:pk>/", LoanApplicationDetailAPIView.as_view(), name="loan-application-detail"),
    path("rejection-reasons/", RejectionReasonListAPIView.as_view(), name="rejection-reason-list"),
    path("rejection-reasons/<int:pk>/", RejectionReasonDetailAPIView.as_view(), name="rejection-reason-detail"),
]
