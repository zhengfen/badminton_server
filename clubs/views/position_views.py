from clubs.models import Position
from clubs.serializers import PositionSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.conf import settings
import json

locales = settings.MODELTRANS_AVAILABLE_LANGUAGES 

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    @action(detail=False)
    def all(self, request):
        serializer = PositionSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        position = Position()        
        name = {}
        for locale in locales:                   
            value = request.data['name'][locale]  
            if value:           
                name[locale] = value

        position.name = name 
        position.save()
        return Response(self.serializer_class(position).data, status=status.HTTP_201_CREATED)

    # use axios.put instead of axios.patch,  TypeError: update() got an unexpected keyword argument 'partial'
    def update(self, request, pk=None):
        position = Position.objects.get(pk = pk)
        name = {} if position.name==None else position.name
        for locale in locales:
            if 'name' in request.data.keys() and locale in request.data['name'].keys():
                value = request.data['name'][locale]  
                if value:            
                    name[locale] = value

        position.name = name
        position.save()
        return Response(self.serializer_class(position).data)

