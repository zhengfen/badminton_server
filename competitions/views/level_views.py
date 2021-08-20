from competitions.models import Level
from competitions.serializers import LevelSerializer

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from django.conf import settings
import json 

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    @action(detail=False)
    def all(self, requset):
        queryset = Level.objects.all()
        serializer = LevelSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # construct title value
        name = {}
        locales = settings.LOCALES
        for locale in locales:
            value = request.data['name'][locale]
            if value:
                name[locale] = value
        
        level = Level.create(name=json.dumps(name)); 
        return Response(self.serializer_class(level).data, status=status.HTTP_201_CREATED)

