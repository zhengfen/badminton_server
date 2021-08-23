from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'clubs'
        ordering = ['name']

    def __str__(self):
        return self.name