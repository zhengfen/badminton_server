from django.db import models
import json

class Role(models.Model):
    name = models.JSONField(blank=True, null=True)
    class Meta:
        db_table = 'roles'

    def __str__(self):
        return json.dumps(self.name)