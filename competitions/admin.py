from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Club, ClubResponsable, Competition, Contact, Game, Group, Level, Player, Structure, Team, Type, User
# Register your models here.
admin.site.register(Club)
admin.site.register(ClubResponsable)
admin.site.register(Competition)
admin.site.register(Contact)
admin.site.register(Group)
admin.site.register(Game)
admin.site.register(Level)
admin.site.register(Structure)
admin.site.register(Team)
admin.site.register(Type)
admin.site.register(User)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('family_name', 'first_name', 'club', 'sex')




