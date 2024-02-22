from django.db import models
from apps.audits.auditing import AuditableMixin
from apps.branches.models import Branch
from apps.common.models import TimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()

class BranchAssets(AuditableMixin, TimeStampedModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True, related_name='branch_assets')
    item = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    brand = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='captured_branch_assets')
    used_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='used_assets')
    purchase_date = models.DateField(null=True, blank=True)
    images = models.JSONField(null=True, blank=True, default=list)

    def __str__(self):
        return f"Branch Asset - ID: {self.id}, Item: {self.item}, Branch: {self.branch}"

    def get_audit_fields(self):
        # Dynamically retrieve all field names from the model
        return [field.name for field in self._meta.fields]