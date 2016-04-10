#!/usr/bin/env python
# encoding: utf-8

from django.db import models


class Horse(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'imię', blank=True, default='')
    age = models.IntegerField(default=0, verbose_name=u'wiek (w miesiącach)')
    birght_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(max_length=255, null=True, blank=True, verbose_name=u'obrazek')
    race = models.ForeignKey('Race', verbose_name=u'rasa', blank=True, null=True)
    # abilities
    agility = models.FloatField(default=0, verbose_name=u'zwinność')
    obedience = models.FloatField(default=0, verbose_name=u'posłuszeństwo')
    stamina = models.FloatField(default=0, verbose_name=u'wytrzymałość')
    strength = models.FloatField(default=0, verbose_name=u'siła')
    speed = models.FloatField(default=0, verbose_name=u'szybkość')
    # training
    dressage = models.FloatField(default=0, verbose_name=u'ujeżdżanie')
    trot = models.FloatField(default=0, verbose_name=u'kłus')
    gallop = models.FloatField(default=0, verbose_name=u'galop')
    canter = models.FloatField(default=0, verbose_name=u'cwał')
    jumping = models.FloatField(default=0, verbose_name=u'skoki')


class Race(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'imię', blank=True, default='')
    image = models.ImageField(max_length=255, null=True, blank=True, verbose_name=u'obrazek')

    agility = models.FloatField(default=0, verbose_name=u'zwinność')
    max_agility = models.FloatField(default=0, verbose_name=u'maksymalna zwinność')
    obedience = models.FloatField(default=0, verbose_name=u'posłuszeństwo')
    max_obedience = models.FloatField(default=0, verbose_name=u'maksymalne posłuszeństwo')
    stamina = models.FloatField(default=0, verbose_name=u'wytrzymałość')
    max_stamina = models.FloatField(default=0, verbose_name=u'maksymalna wytrzymałość')
    strength = models.FloatField(default=0, verbose_name=u'siła')
    max_strength = models.FloatField(default=0, verbose_name=u'maksymalna siła')
    speed = models.FloatField(default=0, verbose_name=u'szybkość')
    max_speed = models.FloatField(default=0, verbose_name=u'maksymalna szybkość')
