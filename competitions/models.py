from django.db import models

class Level(models.Model): 
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'levels'
    def __str__(self):
        return self.name

class Group(models.Model): 
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'groups'
    def __str__(self): 
        return self.name

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

class Type(models.Model): 
    '''
    double men, double women, single man, single woman, double mix
    '''
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'types'
    def __str__(self): 
        return self.name

class Game(models.Model): 
    '''
    Game between players
    '''
    player_h = models.ForeignKey('clubs.User', on_delete=models.PROTECT, related_name='player_home', verbose_name='Player Home')
    player_a = models.ForeignKey('clubs.User', on_delete=models.PROTECT, related_name='player_away', verbose_name='Player Away')
    player_h2 = models.ForeignKey('clubs.User', on_delete=models.PROTECT, blank=True, null=True, related_name='player_home_2')
    player_a2 = models.ForeignKey('clubs.User', on_delete=models.PROTECT, blank=True, null=True, related_name='player_away_2')
    competition = models.ForeignKey(Competition, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
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



