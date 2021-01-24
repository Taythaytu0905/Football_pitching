import uuid

from django.db import models

from football.models import TimeStampedModel


class FilesModel(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'fb_files'
