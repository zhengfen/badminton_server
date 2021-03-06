from django.db import models
from . import User

class Committee(models.Model):
    '''
    member of committee of the association or one club
    subject_type can be : 'Association', 'Club'
    '''
    subject_choices = (
        ('Association', 'Association'),
        ('Club', 'Club')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)    
    subject_type = models.CharField(max_length=255, blank=True, null=True, choices=subject_choices)    
    subject_id = models.PositiveIntegerField(blank=True, null=True)
    title = models.JSONField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='committee', blank=True, null=True)

    class Meta:
        db_table = 'committee'

    def __str__(self):
        return f"{self.title}"