from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from apps.common.models import TimeStampedUserModel

class Note(TimeStampedUserModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')
    note_text = models.TextField()


    def __str__(self):
        return f"Note {self.note_text} for {self.content_object}"

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
