from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin$', views.show_signin),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^users/new$', views.new),
    url(r'^users/edit$', views.edit),
    url(r'^users/show/(?P<id>\d+)$', views.show),
    url(r'^login$', views.login),
    url(r'^create$', views.create),
    url(r'^update$', views.update),
    url(r'^password$', views.password),
    url(r'^users/edit/(?P<id>\d+)$', views.admin_edit),
    url(r'^remove$', views.remove),
    url(r'^destroy', views.destroy)
]
