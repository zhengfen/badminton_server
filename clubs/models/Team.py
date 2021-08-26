from django.db import models
from . import Club

class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    reference = models.CharField(
        max_length=255, unique=True, blank=True, null=True)
    club = models.ForeignKey(Club, related_name='teams',
                             on_delete=models.PROTECT, blank=True, null=True)
    level = models.ForeignKey('competitions.Level',
                              on_delete=models.PROTECT, blank=True, null=True)
    group = models.ForeignKey('competitions.Group',
                              on_delete=models.PROTECT, blank=True, null=True)
    description = models.JSONField(blank=True, null=True)

    # players = models.ManyToManyField(User, through='TeamPlayer')
    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name