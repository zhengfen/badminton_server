from django.db import models
from . import Type

class Game(models.Model): 
    '''
    Game between players
    '''
    player_h = models.ForeignKey('clubs.User', on_delete=models.PROTECT, related_name='player_home', verbose_name='Player Home')
    player_a = models.ForeignKey('clubs.User', on_delete=models.PROTECT, related_name='player_away', verbose_name='Player Away')
    player_h2 = models.ForeignKey('clubs.User', on_delete=models.PROTECT, blank=True, null=True, related_name='player_home_2')
    player_a2 = models.ForeignKey('clubs.User', on_delete=models.PROTECT, blank=True, null=True, related_name='player_away_2')

    type = models.ForeignKey(Type , on_delete=models.PROTECT)   # or Discipline
    score_h_1 = models.PositiveIntegerField(blank=True, null=True)
    score_a_1 = models.PositiveIntegerField(blank=True, null=True)
    score_h_2 = models.PositiveIntegerField(blank=True, null=True)
    score_a_2 = models.PositiveIntegerField(blank=True, null=True)
    score_h_3 = models.PositiveIntegerField(blank=True, null=True)
    score_a_3 = models.PositiveIntegerField(blank=True, null=True)
    match_h = models.PositiveIntegerField(blank=True, null=True)
    match_a = models.PositiveIntegerField(blank=True, null=True)
    set_h = models.PositiveIntegerField(blank=True, null=True)
    set_a = models.PositiveIntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'games'



