from competitions.models import Group
from competitions.serializers import GroupSerializer

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(detail=False)
    def all(self, requset):
        queryset = Group.objects.all()
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)