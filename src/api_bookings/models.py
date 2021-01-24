import uuid

from django.db import models

from api_fields.models import FieldsModels
from football.models import TimeStampedModel
from .constants import Status


class BookingModels(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    date = models.DateTimeField()
    status = models.CharField(max_length=100, choices=Status.STATUS, default=Status.PENDING)
    is_payed = models.BooleanField(default=False)
    field = models.ForeignKey(FieldsModels, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'fb_bookings'
