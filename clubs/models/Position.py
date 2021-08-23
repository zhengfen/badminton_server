from django.db import models

class Position(models.Model):
    '''
    can be: 'captain', 'extra'
    '''
    name = models.CharField(max_length=255, blank=True, null=True)
    class Meta: 
        db_table = 'positions'
    
    def __str__(self):
        return self.name