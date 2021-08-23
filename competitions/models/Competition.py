from django.db import models
from . import Level, Group

class Competition(models.Model):
    '''
    Competition between clubs
    '''
    level = models.ForeignKey(Level, on_delete=models.PROTECT, null=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)
    datatime = models.DateTimeField(null=True)
    turn = models.CharField(max_length=100, blank=True)    
    team_h = models.ForeignKey('clubs.Team', on_delete=models.PROTECT, related_name='team_home', verbose_name='Team Home')
    team_a = models.ForeignKey('clubs.Team', on_delete=models.PROTECT, related_name='team_away', verbose_name='Team Away') 
    matches_h = models.PositiveIntegerField(blank=True, null=True, verbose_name='Match Home')
    matches_a = models.PositiveIntegerField(blank=True, null=True, verbose_name='Match Away')
    set_h = models.PositiveIntegerField(blank=True, null=True)
    set_a = models.PositiveIntegerField(blank=True, null=True)