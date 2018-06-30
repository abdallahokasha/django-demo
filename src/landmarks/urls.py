from django.conf.urls import url
from django.contrib import admin

from .views import (
	landmark_list,
	landmark_create,
	landmark_details,
	)

urlpatterns = [
	url(r'^$', landmark_list),
    url(r'^create/$', landmark_create),
    url(r'^(?P<id>\d+)/$', landmark_details, name='details'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]