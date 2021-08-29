from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from cms.models import Page
from cms.serializers import PageSerializer 

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    @action(detail=False)
    def all(self, request): 
        serializer = PageSerializer(self.queryset, many=True)
        return Response(serializer.data)
