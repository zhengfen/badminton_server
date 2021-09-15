from rest_framework import serializers
from .models import Page, Album

class PageSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Page
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Album
        fields = '__all__'