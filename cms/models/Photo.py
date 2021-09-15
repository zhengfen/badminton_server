from django.db import models
import json
from . import Album

class Photo(models.Model):
    reference = models.CharField(max_length=255, blank=True, null=True)
    title = models.JSONField(blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='photos', blank=True, null=True)
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        db_table = 'photos'
        ordering = ['order', 'id']

    def __str__(self): 
        return json.dumps(self.title)
