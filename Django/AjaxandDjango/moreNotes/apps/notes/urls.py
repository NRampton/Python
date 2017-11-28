from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^edit/', views.edit),
    url(r'^select/', views.select),
    url(r'^destroy/', views.destroy),
    url(r'^create/', views.create),
]
