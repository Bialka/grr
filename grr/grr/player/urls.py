#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from grr.player import views

urlpatterns = [
    url(r'^profil$', views.profile, name='profile'),
    url(r'^ustawienia$', views.player_settings, name='player_settings'),
    url(r'^znajomi$', views.friends, name='friends'),
]