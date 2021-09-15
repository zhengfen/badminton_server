from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from cms.models import Album, Photo
from cms.serializers import AlbumSerializer 

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @action(detail=False)
    def all(self, request): 
        serializer = AlbumSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods='POST')
    def photos(self, request): 
        """
        save photos from album drop zone
        """
        if request.images:
            album = self.get_object()
            for f in request.FILES.getlist('images'): 
                filename = f.name
                photo, created = Photo.objects.get_or_create(album_id=album.id, reference=filename)
                # TODO: store image file for the photo
                
        
            