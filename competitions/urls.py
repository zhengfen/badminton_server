from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('levels', views.LevelViewSet, basename="level")
router.register('groups', views.GroupViewSet, basename="group")
urlpatterns = [
    path('', include(router.urls)),
    path('seed/levels', views.seed_levels), 
]