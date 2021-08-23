from django.db import models

class Type(models.Model): 
    '''
    double men, double women, single man, single woman, double mix
    '''
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'types'
        ordering = ['name']

    def __str__(self): 
        return self.name