from django.db import models

class Group(models.Model): 
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'groups'
        ordering = ['name']

    def __str__(self): 
        return self.name