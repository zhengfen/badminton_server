from django.db import models
from . import Team, User, Position

class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, related_name='team_players', on_delete=models.CASCADE)
    player = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)    
    position = models.ForeignKey(Position, on_delete=models.PROTECT, blank=True, null=True)
    class Meta:
        db_table = 'team_player'
        unique_together = ['team', 'player']

    def __str__(self):
        return f"{self.team.name} {self.user.first_name} {self.user.last_name}"