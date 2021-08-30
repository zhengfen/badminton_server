from django.db import models
import json

class Page(models.Model):
    title = models.JSONField(blank=True, null=True)
    content = models.JSONField(blank=True, null=True)
    on_menu = models.BooleanField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    class Meta:
        db_table = 'pages'
        ordering = ['order', 'id']

    def __str__(self): 
        return json.dumps(self.title)
