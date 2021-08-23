from django.db import models
from modeltrans.fields import TranslationField

class Level(models.Model): 
    name = models.CharField(max_length=255, blank=True, null=True)

    i18n = TranslationField(fields=("name", ))

    class Meta:
        db_table = 'levels'
        ordering = ['name']

    def __str__(self):
        return self.name