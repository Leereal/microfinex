from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.branches.models import Branch
from apps.common.models import TimeStampedModel

User = get_user_model()

class UserBranch(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_branches')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='user_branches')
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_user_branches')

    class Meta:
        unique_together = ('user', 'branch')  # Ensure uniqueness of user-branch combination

    def __str__(self):
        return f"{self.user} - {self.branch}"