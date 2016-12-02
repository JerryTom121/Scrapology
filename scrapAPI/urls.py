from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.tw_form, name='twform'),
    url(r'^twusers/$', views.twusers_list),
    url(r'^twusers/(?P<username>[A-Za-z0-9_]+)$', views.twuser_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)