from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes

from clubs.models import Role
from clubs.serializers import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    '''
    list is needed for selection
    '''
    @action(detail=False)    
    def all(self, request):
        queryset = Role.objects.all().order_by('name')
        serializer = RoleSerializer(queryset, many=True)
        return Response(serializer.data)