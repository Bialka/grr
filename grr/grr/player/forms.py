#!/usr/bin/env python
# encoding: utf-8

from django import forms

from .models import Player

class PlayerSettingsForm(forms.ModelForm):
    
    class Meta:
        model = Player
        fields = ['avatar', 'friends']
