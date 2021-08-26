from django.http import HttpResponse
from clubs.models import Club, ClubResponsible, Contact, User
from clubs.serializers import PlayerWithTeamsSerializer

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet): 
    serializer_class = PlayerWithTeamsSerializer
    # permission_classes = [IsAdminUser, ]
    def get_queryset(self):
        queryset = User.objects.all()
        filers = ['club']
        for filter in filers: 
            value = self.request.query_params.get(filter)        
            if value is not None:
                queryset = queryset.filter(**{filter: value})
        
        value = self.request.query_params.get('search')
        if value is not None:
            queryset = queryset.filter(Q(first_name__icontains=value)|Q(last_name__icontains=value)|Q(email_icontains=value))
        return queryset
