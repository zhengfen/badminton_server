from clubs.models import TeamPlayer
from clubs.serializers import TeamPlayerSerializer, TeamPlayerWithTeamSerializer, TeamPlayerWithPlayerSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class TeamPlayerViewSet(viewsets.ModelViewSet):
    queryset = TeamPlayer.objects.all()
    serializer_class = TeamPlayerSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            team_player, created = TeamPlayer.objects.get_or_create(**serializer.validated_data)            
            if 'with' in request.data.keys():                
                if (request.data['with'] == 'team'):
                    new_serializer = TeamPlayerWithTeamSerializer
                else: 
                    new_serializer = TeamPlayerWithPlayerSerializer
            else:
                new_serializer = self.serializer_class
            
            return Response(new_serializer(team_player).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
