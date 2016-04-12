#!/usr/bin/env python
# encoding: utf-8

from annoying.decorators import render_to
from django.shortcuts import get_object_or_404

from .models import Horse, Race

@render_to('horse/horse.html')
def horse(request, horse_id):
    horse = get_object_or_404(Horse, id=horse_id)
    return {
        'horse': horse,
    }


@render_to('horse/race.html')
def race(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    return {
        'race': race,
    }
