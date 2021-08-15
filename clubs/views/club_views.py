from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from clubs.models import Club, ClubResponsable, Contact, Team, User
from clubs.serializers import ClubSerializer, ClubResponsableSerializer, ClubWithTeamsSerializer, TeamSerializer, TeamWithPlayerUserSerializer 

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated



# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
class ClubViewSet(viewsets.ModelViewSet):
    
    perms_map = {
        'get': '*', 
        'post': 'club_create', 
        'put': 'club_update', 
        'delete': 'club_delete',
    }
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    search_fields = ['name']
    ordering_fields = ['name']   

    @action(detail=False)    
    @permission_classes([IsAuthenticated])
    def all(self, requset):
        queryset = Club.objects.all()
        serializer = ClubSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def show(self, request, pk=None):
        club = get_object_or_404(Club, pk=pk)
        club_s = ClubSerializer(club)

        responsables = club.responsables
        responsables_s = ClubResponsableSerializer(responsables, many=True)

        teams = club.teams.order_by('name')
        teams_s = TeamWithPlayerUserSerializer(teams, many=True)

        return Response({
            'club': club_s.data,
            'responsables': responsables_s.data,
            'teams': teams_s.data
        })
