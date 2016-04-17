#!/usr/bin/env python
# encoding: utf-8

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class Player(models.Model):
    user = models.OneToOneField(User, related_name='player',
        verbose_name=u'użytkownik',blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    friends = models.ManyToManyField(User, verbose_name=u'znajomi',
        related_name='friends')

    money = models.IntegerField(verbose_name=u'pieniądze', default=2000)


@receiver(models.signals.post_save, sender=User)
def create_player(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        try:
            Player.objects.create(user=user)
        except DatabaseError:
            pass
