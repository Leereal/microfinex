from django.urls import path
from .views import AddChargeView, RefundView, BonusView, TopUpView

urlpatterns = [
    path('add-charge/', AddChargeView.as_view(), name='add_charge'),
    path('refund/', RefundView.as_view(), name='refund'),
    path('bonus/', BonusView.as_view(), name='bonus'),
    path('top-up/', TopUpView.as_view(), name='top_up'),
]
