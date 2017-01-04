from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', entry1),
    url(r'^(?P<blog_id>[0-9]+)', entry2),
    url(r'^all/$', all_entries),
    url(r'^all/user/(?P<userId>[0-9]+)$', show_all_entries),
]
