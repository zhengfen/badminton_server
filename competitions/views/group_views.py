from competitions.models import Group
from competitions.serializers import GroupSerializer
from rest_framework import viewsets

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer