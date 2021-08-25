from django.db import models
import json

class Position(models.Model):
    '''
    can be: 'captain', 'extra'
    '''
    name = models.JSONField(blank=True, null=True)    
    class Meta: 
        db_table = 'positions'
    
    def __str__(self):
        return json.dumps(self.name)