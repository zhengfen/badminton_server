from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from clubs.models import Club, ClubResponsable, Contact, Structure, Team, User
from clubs.serializers import ClubSerializer, ClubResponsableSerializer, ClubWithStructuresSerializer, ClubWithTeamsSerializer, StructureSerializer, TeamSerializer, TeamWithPlayerUserSerializer 

from rest_framework.response import Response
from rest_framework import viewsets, status


# Create your views here.


class ClubViewSet(viewsets.ModelViewSet):
    
    perms_map = {
        'get': '*', 
        'post': 'club_create', 
        'put': 'club_update', 
        'delete': 'club_delete',
    }
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    pagination_class = None
    search_fields = ['name']
    ordering_fields = ['name']   
    

    def list(self, request):
        clubs = Club.objects.all()
        clubs_s = ClubWithStructuresSerializer(clubs, many=True)

        structures = Structure.objects.all()
        structures_s = StructureSerializer(structures, many=True)
        return Response({
            'clubs': clubs_s.data,
            'structures': structures_s.data
        })

    def retrieve(self, request, pk=None):
        club = get_object_or_404(Club, pk=pk)
        club_s = ClubSerializer(club)

        responsables = club.responsables
        responsables_s = ClubResponsableSerializer(responsables, many=True)

        teams = club.teams
        teams_s = TeamWithPlayerUserSerializer(teams, many=True)

        return Response({
            'club': club_s.data,
            'responsables': responsables_s.data,
            'teams': teams_s.data
        })
