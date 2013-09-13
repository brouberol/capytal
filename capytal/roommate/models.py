# -*- coding: utf-8 -*-

"""
Models related to the collocation members
"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Roommate(models.Model):
    balance = models.FloatField(default=0.0, verbose_name=u'solde')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'colocataire'
        verbose_name_plural = 'colocataires'


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Roommate.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)
