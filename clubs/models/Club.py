from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    class Meta:
        db_table = 'clubs'

    def __str__(self):
        return self.name