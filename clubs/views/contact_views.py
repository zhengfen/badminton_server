
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes

from clubs.models import Contact
from clubs.serializers import ContactSerializer, ContactWithUserSerializer

from django.db.models import Q

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer

    def get_queryset(self):
        queryset = Contact.objects.all()
        filers = []
        for filter in filers: 
            value = self.request.query_params.get(filter)        
            if value is not None:
                queryset = queryset.filter(**{filter: value})
        
        # search
        # Choices are: address, city, id, image, npa, phone, user, user_id
        value = self.request.query_params.get('search')
        if value is not None:
            queryset = queryset.filter(Q(user__first_name__icontains=value) | Q(user__last_name__icontains=value))
        return queryset.order_by('-id')

    def list(self, request, *args, **kwargs):
        '''
        override list function to get contacts with user
        '''
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ContactWithUserSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ContactWithUserSerializer(queryset, many=True)
        return Response(serializer.data)

