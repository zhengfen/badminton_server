from django.urls import path, include
from . import views 

from rest_framework import routers

router = routers.DefaultRouter()

router.register('pages', views.PageViewSet, basename="pages")

urlpatterns = [
    path('', include(router.urls)),
    path('seed/pages', views.seed_pages),
]