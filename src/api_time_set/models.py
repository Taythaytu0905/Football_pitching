import uuid

from django.db import models

from api_yarns.models import YarnsModels
from football.models import TimeStampedModel


class TimeSetModels(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField()
    belongs_yarn = models.ForeignKey(YarnsModels, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'fb_time_set'
