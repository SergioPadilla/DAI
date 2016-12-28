"""
Created at 19/12/16
__author__ = 'Sergio Padilla'
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
]
