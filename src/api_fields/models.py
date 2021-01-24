import uuid

from django.db import models

from api_yarns.models import YarnsModels
from football.models import TimeStampedModel


class FieldsModels(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    price = models.FloatField()
    belongs_yarn = models.ForeignKey(YarnsModels, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'fb_fields'
