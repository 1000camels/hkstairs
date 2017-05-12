from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'stair', views.StairViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^json/(?P<stairid>[\w-]+)/$', views.get_stairs, name='stair_json'),
    url(r'^stairs/', views.stair_set, name='stair_set'),
    url(r'^', include(router.urls)),
]
