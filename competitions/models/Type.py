from django.db import models

class Type(models.Model): 
    '''
    double men, double women, single man, single woman, double mix
    '''
    name = models.JSONField(blank=True, null=True)
    class Meta:
        db_table = 'types'
        ordering = ['id']

    def __str__(self): 
        return self.name