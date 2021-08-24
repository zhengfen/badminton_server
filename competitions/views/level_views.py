from competitions.models import Level
from competitions.serializers import LevelSerializer

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from django.conf import settings
import logging
logger = logging.getLogger(__name__)

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    @action(detail=False)
    def all(self, requset):
        queryset = Level.objects.all()
        serializer = LevelSerializer(queryset, many=True)
        return Response(serializer.data)



