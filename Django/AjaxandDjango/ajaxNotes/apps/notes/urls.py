from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/', views.create),
    url(r'^select', views.select),
    url(r'^update/', views.update),
    url(r'^destroy/', views.destroy)
]
