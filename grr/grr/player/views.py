#!/usr/bin/env python
# encoding: utf-8

from django.core.urlresolvers import reverse
from annoying.decorators import render_to
from django.shortcuts import redirect

from .forms import PlayerSettingsForm

@render_to('player/profile.html')
def profile(request):
    return {
        'user': request.user,
        'player': request.player,
    }


@render_to('player/player_settings.html')
def player_settings(request):
    form = PlayerSettingsForm(request.POST or None)
    if form.is_valid():
        form.save()
        redirect(reverse('player:profile'))

    return {
        'form': form,
    }


@render_to('player/friends.html')
def friends(request):
    return {
        'friends': request.player.friends.all(),
    }
