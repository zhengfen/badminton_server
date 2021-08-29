from django.db import models
import json

class Page(models.Model):
    title = models.JSONField(blank=True, null=True)
    content = models.JSONField(blank=True, null=True)
    class Meta:
        db_table = 'pages'

    def __str__(self): 
        return json.dumps(self.title)
