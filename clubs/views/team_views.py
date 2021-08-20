
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from clubs.models import Club, Team
from clubs.serializers import TeamSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from openpyxl import load_workbook
import os


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



def import_teams(request):
    '''
    get teams from excel 
    B(4, 10)  level_id 5
    B(12, 20) level_id 6
    E(12, 19) level_id 6
    B(22, 29) level_id 7
    E(22, 27) level_id 7
    '''
    filename = os.path.join(settings.BASE_DIR, 'excels/Interclub 2020 - 2021.xlsx')
    wb = load_workbook(filename = filename)
    sh = wb['Equipes']

    groups= [
        {
            'first_column': 'B', 
            'start':4,
            'stop': 10,
            'level_id': 5
        }, 
        {
            'first_column': 'B', 
            'start':12,
            'stop': 20,
            'level_id': 6
        }, 
        {
            'first_column': 'E', 
            'start':12,
            'stop': 19,
            'level_id': 6
        }, 
        {
            'first_column': 'B', 
            'start':22,
            'stop': 29,
            'level_id': 7
        }, 
        {
            'first_column': 'E', 
            'start':22,
            'stop': 27,
            'level_id': 7
        }, 
    ]

    for group in groups:
        for i in range(group['start'], group['stop']):
            txt = sh[group['first_column'] + str(i)].value
            if (txt): 
                [reference, team_name] = txt.split(' ', 1)
                # team
                team, created = Team.objects.get_or_create(name=team_name)
                team.reference = reference
                team.level_id = group['level_id']
                team.save()


    return HttpResponse("Done")

def process_teams(request):
    '''
    try to add club_id by analysing names
    '''
    teams = Team.objects.filter(club_id__isnull=True)
    for team in teams:
        team_name = team.name.split()[0]
        club = Club.objects.filter(name__icontains=team_name).first()
        if club: 
            team.club_id = club.id
            team.save()
    return HttpResponse("Done")