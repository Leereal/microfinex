# from rest_framework import serializers
# from apps.countries.models import Country
# from .models import GroupProductCharge
# from apps.charges.serializers import ChargeSerializer
# from rest_framework.validators import UniqueTogetherValidator


# class GroupProductSerializer(serializers.ModelSerializer):
#     charge = ChargeSerializer(read_only=True)

#     class Meta:
#         model = GroupProductCharge
#         fields = [
#             "id",
#             "group_product",
#             "charge",
#             "is_active",      
#         ]

#         validators = [
#             UniqueTogetherValidator(
#                 queryset=GroupProductCharge.objects.all(),
#                 fields=['list', 'position']
#             )
#         ]
     