from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Club, ClubResponsible, Contact, Member, Position, Role, Team, User
# Register your models here.

admin.site.register(Position)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
 

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin): 
    list_display = ('name', 'city')

@admin.register(ClubResponsible)
class ClubResponsibleAdmin(admin.ModelAdmin): 
    list_display = ('id', 'club', 'function', 'user')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin): 
    list_display = ('user', 'phone', 'address', 'npa', 'city')
    search_field = ('phone', 'address', 'npa', 'city')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'club', 'level', 'group')
    search_fields = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin): 
    list_display = ('id', 'first_name', 'last_name', 'sex', 'birthday', 'club', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin): 
    list_display = ('id', 'user', 'title', 'subject_type', 'subject_id', 'image')
    search_fields = ('title', 'subject_type')