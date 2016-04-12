#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^kon/(?P<horse_id>\d+)$', views.horse, name='horse'),
    url(r'^rasa/(?P<race_id>\d+)$', views.race, name='race'),
]


