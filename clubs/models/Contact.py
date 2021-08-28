from django.db import models
from . import User

class Contact(models.Model):
    user = models.OneToOneField(
        User, related_name='contact', on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    npa = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='contacts', blank=True, null=True)
    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" 