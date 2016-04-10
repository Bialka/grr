#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin

from .models import Horse, Race

admin.site.register(Horse)
admin.site.register(Race)
