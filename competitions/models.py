from django.db import models
from django.contrib.auth.models import AbstractUser


        

class User(AbstractUser):    
    first_name= models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    class Meta:
        db_table = 'auth_user'

class Contact(models.Model):
    user = models.OneToOneField(User, related_name='contact', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    npa = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self): 
        return self.user.username

class Structure(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self): 
        return self.name


class Club(models.Model): 
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    structures = models.ManyToManyField(Structure, blank=True)
    def __str__(self): 
        return self.name
    class Meta: 
        ordering = ['name']


class ClubResponsable(models.Model): 
    club = models.ForeignKey(Club, related_name='responsables', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    function = models.CharField(max_length=255, blank=True, null=True) 
    def __str__(self): 
        return self.club.name + '_' + self.user.username

class Level(models.Model): 
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Group(models.Model): 
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self): 
        return self.name

class Player(models.Model):
    sex_choices = (
        ('M', 'Male'), 
        ('F', 'Female')
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    family_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    licence = models.CharField(max_length=255, unique=True)
    club = models.ForeignKey(Club, on_delete=models.PROTECT, null=True) 
    sex = models.CharField(max_length=20, blank=True, null=True, choices=sex_choices)
    birthday = models.DateField(blank=True, null=True)
    def __str__(self): 
        return '%s %s' % (self.family_name, self.first_name)

class Team(models.Model): 
    name = models.CharField(max_length=255, unique=True)    
    reference = models.CharField(max_length=255, unique=True, blank=True, null=True)  
    club = models.ForeignKey(Club, related_name='teams', on_delete=models.PROTECT, null=True) 
    players = models.ManyToManyField(Player, blank=True)    
    level = models.ForeignKey(Level, on_delete=models.PROTECT, null=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)
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
    team_h = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_home', verbose_name='Team Home')
    team_a = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_away', verbose_name='Team Away') 
    matches_h = models.PositiveIntegerField(blank=True, null=True, verbose_name='Match Home')
    matches_a = models.PositiveIntegerField(blank=True, null=True, verbose_name='Match Away')
    set_h = models.PositiveIntegerField(blank=True, null=True)
    set_a = models.PositiveIntegerField(blank=True, null=True)

class Type(models.Model): 
    '''
    double men, double women, single man, single woman, double mix
    '''
    name = models.CharField(max_length=100)
    def __str__(self): 
        return self.name

class Game(models.Model): 
    '''
    Game between players
    '''
    player_h = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='player_home', verbose_name='Player Home')
    player_a = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='player_away', verbose_name='Player Away')
    player_h2 = models.ForeignKey(Player, on_delete=models.PROTECT, blank=True, null=True, related_name='player_home_2')
    player_a2 = models.ForeignKey(Player, on_delete=models.PROTECT, blank=True, null=True, related_name='player_away_2')
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



