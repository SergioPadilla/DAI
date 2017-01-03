"""
Created at 19/12/16
__author__ = 'Sergio Padilla'
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^me/$', views.me, name='me'),
    url(r'^examples/$', views.examples, name='examples'),
    url(r'^highcharts/$', views.highcharts, name='highcharts'),
    url(r'^mongo_examples/$', views.find, name='mongo_examples'),
    # url(r'^find/$', views.find, name='find'),
]
