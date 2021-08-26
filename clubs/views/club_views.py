from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from clubs.models import Club, ClubResponsible, Contact, Team, User
from clubs.serializers import ClubSerializer, ClubResponsibleSerializer, ClubWithTeamsSerializer, TeamSerializer, TeamWithPlayerUserSerializer 

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated



# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = ClubSerializer

    def get_queryset(self):
        queryset = Club.objects.all()
        filers = []
        for filter in filers: 
            value = self.request.query_params.get(filter)        
            if value is not None:
                queryset = queryset.filter(**{filter: value})
        
        # search
        value = self.request.query_params.get('search')
        if value is not None:
            queryset = queryset.filter(name__icontains=value)
        return queryset.order_by('-id')

    @action(detail=False)    
    # @permission_classes([IsAuthenticated])
    def all(self, requset):
        queryset = Club.objects.all().order_by('name')
        serializer = ClubSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def show(self, request, pk=None):
        club = get_object_or_404(Club, pk=pk)
        club_s = ClubSerializer(club)

        responsables = club.responsables
        responsables_s = ClubResponsibleSerializer(responsables, many=True)

        teams = club.teams.order_by('name')
        teams_s = TeamWithPlayerUserSerializer(teams, many=True)

        return Response({
            'club': club_s.data,
            'responsables': responsables_s.data,
            'teams': teams_s.data
        })
