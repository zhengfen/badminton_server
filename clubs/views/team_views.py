from django.shortcuts import render, get_object_or_404

from clubs.models import Club, Team
from clubs.serializers import TeamSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


'''
https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
'''
class TeamViewSet(viewsets.ModelViewSet):
    # queryset = Team.objects.all()
    serializer_class = TeamSerializer
    # permission_classes = [IsAdminUser, ]
    def get_queryset(self):
        '''
        get teams by filters
        '''
        queryset = Team.objects.all()
        filers = ['club', 'level', 'group']
        for filter in filers: 
            value = self.request.query_params.get(filter)        
            if value is not None:
                queryset = queryset.filter(**{filter: value})
        
        value = self.request.query_params.get('search')
        if value is not None:
            queryset = queryset.filter(name__icontains=value)
        return queryset
    
    @action(detail=True)
    def show(self, request, pk=None):
        team = get_object_or_404(Team, pk=pk)
        team_s = TeamSerializer(team)
        # TODO get players

    @action(detail=False)
    def all(self, request):
        queryset = self.get_queryset()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)