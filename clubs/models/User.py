from django.db import models
from django.contrib.auth.models import AbstractUser
from . import Club

class User(AbstractUser):
    sex_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True, null=True, blank=True, max_length=100)
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)   
    licence = models.CharField(max_length=255, unique=True, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True,
                           null=True, choices=sex_choices)
    birthday = models.DateField(blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.PROTECT, blank=True, null=True)
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Contact(models.Model):
    user = models.OneToOneField(
        User, related_name='contact', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    npa = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return self.user.username