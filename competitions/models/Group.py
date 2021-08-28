from django.db import models

class Group(models.Model): 
    name = models.JSONField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'groups'

    def __str__(self): 
        return self.name