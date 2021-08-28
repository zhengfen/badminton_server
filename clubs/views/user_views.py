from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes

from clubs.models import Contact, User
from clubs.serializers import UserSerializer, UserWithTeamsSerializer

from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet): 
    serializer_class = UserSerializer
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
            queryset = queryset.filter(Q(first_name__icontains=value)|Q(last_name__icontains=value)|Q(email__icontains=value))
        return queryset.order_by('-id')

    
    def list(self, request, *args, **kwargs):
        '''
        override list function to get users with teams
        '''
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserWithTeamsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = UserWithTeamsSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)   
    def search(self, request, *args, **kwargs):
        queryset = User.objects.all()
        value = self.request.query_params.get('search')
        if value is not None:
            queryset = queryset.filter(Q(first_name__icontains=value)|Q(last_name__icontains=value)|Q(email__icontains=value))
        queryset = queryset.order_by('first_name')[:10]
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)




