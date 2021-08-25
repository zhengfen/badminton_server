from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Club, ClubResponsible, Contact, Position, Team, User
# Register your models here.

admin.site.register(Position)
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin): 
    list_display = ('name', 'city')

@admin.register(ClubResponsible)
class ClubResponsibleAdmin(admin.ModelAdmin): 
    list_display = ('id', 'club', 'function', 'user')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin): 
    list_display = ('user', 'phone', 'address', 'npa', 'city')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'club', 'level', 'group')


@admin.register(User)
class UserAdmin(admin.ModelAdmin): 
    list_display = ('id', 'first_name', 'last_name', 'sex', 'birthday', 'club')
