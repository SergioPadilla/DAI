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
    url(r'^findpage/$', views.findpage, name='findpage'),
    url(r'^find/$', views.find, name='find'),
    url(r'^get_borough_data/$', views.get_borough_data, name='get_borough_data'),
]
