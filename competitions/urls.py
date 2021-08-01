from rest_framework import routers
from django.urls import path, include
from competitions import views

router = routers.DefaultRouter()
router.register('clubs', views.ClubViewSet)
router.register('teams', views.TeamViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('parse/responsables', views.parse_responsables),
    path('parse/teams', views.parse_teams),
    path('process/teams', views.process_teams)
]