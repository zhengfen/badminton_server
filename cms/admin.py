from django.contrib import admin
from .models import Page, Album, Photo
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_field = ('title', 'content')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_field = ('title', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin): 
    list_display = ('reference', 'title', 'description', 'image')
    search_field = ('reference', 'title', 'description')
