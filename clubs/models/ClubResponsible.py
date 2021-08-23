from django.db import models
from . import Club, User

class ClubResponsable(models.Model):
    club = models.ForeignKey(
        Club, related_name='responsables', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    function = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'club_responsible'

    def __str__(self):
        return self.club.name + '_' + self.user.username