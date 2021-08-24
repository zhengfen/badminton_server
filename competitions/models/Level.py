from django.db import models
import json

class Level(models.Model): 
    name = models.JSONField(blank=True, null=True)

    translatable = ['name']

    class Meta:
        db_table = 'levels'
        ordering = ['id']

    def __str__(self):
        return json.dumps(self.name)