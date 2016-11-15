from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tw_form, name='twform'),
]