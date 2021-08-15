from clubs.models import Position
from clubs.serializers import PositionSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    @action(detail=False)
    def all(self, request):
        serializer = PositionSerializer(self.queryset, many=True)
        return Response(serializer.data)
