from django.db import models
import json

class Album(models.Model):
    title = models.JSONField(blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)