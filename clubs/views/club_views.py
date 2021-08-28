from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.utils.text import slugify

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from clubs.models import Club, ClubResponsible, Contact, Team, User
from clubs.serializers import ClubSerializer, ClubResponsibleSerializer, ClubWithTeamsSerializer, TeamSerializer, TeamWithPlayerUserSerializer 



# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = ClubSerializer
    
    # @permission_classes([IsAuthenticated])
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

    '''
    override create function to add slug 
    '''
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        club = self.perform_create(serializer)
        # add slug
        club.slug = slugify(club.name)
        club.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    '''
    list is needed for club selection and ClubIndex.vue (id, name, slug is needed)
    '''
    @action(detail=False)    
    def all(self, request):
        queryset = Club.objects.all().order_by('name')
        serializer = ClubSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def club_show(request, slug=None):
    club = get_object_or_404(Club, slug=slug)
    club_s = ClubSerializer(club)

    responsibles = club.responsibles
    responsibles_s = ClubResponsibleSerializer(responsibles, many=True)

    teams = club.teams.order_by('name')
    teams_s = TeamWithPlayerUserSerializer(teams, many=True)

    return Response({
        'club': club_s.data,
        'responsibles': responsibles_s.data,
        'teams': teams_s.data
    })
