from django.contrib import admin
from .models import Group, Game, Level, Type


admin.site.register(Group)
admin.site.register(Game)
admin.site.register(Level)
admin.site.register(Type)