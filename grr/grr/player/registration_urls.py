#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from grr.player import registration_views

urlpatterns = [
    url(r'^$', registration_views.home, name='home'),

    url(r'^zaloguj/$', auth_views.login, name='login'),
    url(r'^wyloguj/$', auth_views.logout, name='logout'),
    url(r'^zmiana_hasla/$', auth_views.password_change, name='password_change'),
    url(r'^zmiana_hasla/juz/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^reset_hasla/$', auth_views.password_reset, name='password_reset'),
    url(r'^reset_hasla/juz/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/juz/$', auth_views.password_reset_complete, name='password_reset_complete'),
]