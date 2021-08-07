from competitions.models import Level
from competitions.serializers import LevelSerializer
from rest_framework import viewsets

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

