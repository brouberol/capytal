"""
URLConfig of the roommate app
"""

from django.conf.urls import patterns, url

from .views import RoommateListView
from .views import RoommateCreateView
from .views import RoommateUpdateView
from .views import RoommateDetailView


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$', RoommateDetailView.as_view(), name="roommate-display"),
    url(r'^$', RoommateListView.as_view(), name="roommate-list"),
    url(r'^new$', RoommateCreateView.as_view(), name="roommate-create"),
    url(r'^(?P<pk>\d+)/update$', RoommateUpdateView.as_view(), name="roommate-update"),
)
