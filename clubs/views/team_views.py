
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.conf import settings

from clubs.models import Club, Team
from clubs.serializers import TeamSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

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


def import_teams(request):
    '''
    get teams from excel 
    B(4, 10)  level_id 5
    B(12, 20) level_id 6
    E(12, 19) level_id 6
    B(22, 29) level_id 7
    E(22, 27) level_id 7
    '''
    filename = os.path.join(settings.BASE_DIR, 'Interclub 2020 - 2021.xlsx')
    wb = load_workbook(filename = filename)
    sh = wb['Equipes']

    for i in range(22, 27):
        txt = sh['E' + str(i)].value
        if (txt): 
            [reference, team_name] = txt.split(' ', 1)
            # team
            team, created = Team.objects.get_or_create(name=team_name)
            team.reference = reference
            team.level_id = 7
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