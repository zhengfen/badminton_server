from django.urls import path, include
from . import views

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('clubs', views.ClubViewSet, basename="club")
router.register('teams', views.TeamViewSet, basename="team")
router.register('players', views.PlayerViewSet, basename="player")

urlpatterns = [
    path('', include(router.urls)),    
    path('excel/import/responsables', views.import_responsables),
    path('excel/import/teams', views.import_teams),
    path('process/teams', views.process_teams),
    path('process/users', views.process_users)
]

# urlpatterns = format_suffix_patterns(urlpatterns)