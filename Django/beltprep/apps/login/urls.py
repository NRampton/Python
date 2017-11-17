from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^reg$', views.createUser),
    url(r'^users/(?P<id>\d+)$', views.display_user),
    url(r'^logout$', views.logout)
]
