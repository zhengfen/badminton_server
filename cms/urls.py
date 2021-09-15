from django.urls import path, include
from . import views 

from rest_framework import routers

router = routers.DefaultRouter()

router.register('pages', views.PageViewSet, basename="pages")
router.register('albums', views.AlbumViewSet, basename="albums")

urlpatterns = [
    path('', include(router.urls)),
    # path('seed/pages', views.seed_pages), #  use fixtures to pre-populate datebase
]