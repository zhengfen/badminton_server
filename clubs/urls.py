from django.urls import path, include
from . import views

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()

router.register('roles', views.RoleViewSet, basename="roles")
router.register('clubs', views.ClubViewSet, basename="clubs")
router.register('users', views.UserViewSet, basename="users")
router.register('teams', views.TeamViewSet, basename="teams")
router.register('positions', views.PositionViewSet, basename="positions")
router.register('team-player', views.TeamPlayerViewSet, basename="team-player")
router.register('contacts', views.ContactViewSet, basename="contacts")

urlpatterns = [
    path('', include(router.urls)),   
    path('club/<slug:slug>', views.club_show),
    path('import/responsibles', views.import_responsibles),
    path('import/teams', views.import_teams),
    path('process/teams', views.process_teams),
    path('process/users', views.process_users),
    path('process/clubs', views.process_clubs),
    path('seed/positions', views.seed_positions), 
    path('seed/roles', views.seed_roles)
]

# urlpatterns = format_suffix_patterns(urlpatterns)