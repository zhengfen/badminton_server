from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'clubs'
        ordering = ['name']

    def __str__(self):
        return self.name

class User(AbstractUser):
    sex_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True, null=True, blank=True, max_length=100)
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)   
    licence = models.CharField(max_length=255, unique=True, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True,
                           null=True, choices=sex_choices)
    birthday = models.DateField(blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.PROTECT, blank=True, null=True)
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS
    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contact(models.Model):
    user = models.OneToOneField(
        User, related_name='contact', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    npa = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return self.user.username


class ClubResponsable(models.Model):
    club = models.ForeignKey(
        Club, related_name='responsables', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    function = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'club_responsible'

    def __str__(self):
        return self.club.name + '_' + self.user.username


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

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name

class TeamPlayer(models.Model):
    '''
    role can be: 'captain', 'joker'
    '''
    team = models.ForeignKey(Team, related_name='team_players', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)    
    role = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'team_player'

    def __str__(self):
        return f"{self.team.name} {self.user.first_name} {self.user.last_name}"
