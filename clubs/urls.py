from django.urls import path, include
from . import views

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('clubs', views.ClubViewSet, basename="clubs")
router.register('teams', views.TeamViewSet, basename="teams")
router.register('players', views.PlayerViewSet, basename="players")
router.register('positions', views.PositionViewSet, basename="positions")
router.register('team-player', views.TeamPlayerViewSet, basename="team-player")

urlpatterns = [
    path('', include(router.urls)),    
    path('import/responsables', views.import_responsibles),
    path('import/teams', views.import_teams),
    path('process/teams', views.process_teams),
    path('process/users', views.process_users)
]

# urlpatterns = format_suffix_patterns(urlpatterns)