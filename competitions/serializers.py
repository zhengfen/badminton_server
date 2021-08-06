from rest_framework import serializers
from .models import Competition, Game, Group, Type




class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'





