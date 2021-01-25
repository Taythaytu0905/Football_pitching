import uuid

from django.db import models

from api_files.models import FilesModel
from api_users.models import CustomUser
from football.models import TimeStampedModel


class YarnsModels(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    images = models.ManyToManyField(FilesModel, related_name="image_tour", blank=True, null=True)
    policy = models.TextField(null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    drink = models.FloatField(default=0)
    park = models.FloatField(default=0)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'fb_yarns'
