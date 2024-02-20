from django.db import models
from apps.common.models import TimeStampedModel

class Document(TimeStampedModel):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    loan = models.ForeignKey('Loan', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    document_type = models.ForeignKey('DocumentType', on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey('User', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
