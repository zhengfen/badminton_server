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

    # TypeError: 'Level' object does not support item assignment
    def create(self, request):
        level = Level()
        locales = settings.MODELTRANS_AVAILABLE_LANGUAGES 
        for locale in locales:
            if 'name_' + locale in request.data.keys():           
                value = request.data['name_' + locale]            
                setattr(level, 'name_'  + locale, value)
        level.save()
        return Response(self.serializer_class(level).data, status=status.HTTP_201_CREATED)

