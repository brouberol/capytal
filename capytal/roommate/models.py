# -*- coding: utf-8 -*-

"""
Models related to the collocation members
"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from expense.models import Expense


class Roommate(models.Model):
    balance = models.FloatField(default=0.0, verbose_name=u'solde')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    expenses = models.ManyToManyField(
        Expense, related_name='+', verbose_name=u'dépenses', blank=True)

    def _repr_balance(self):
        return str(self.balance) if self.balance > 0 else '-%s' % (str(self.balance))

    def __unicode__(self):
        return '%s %s' % (self.user.username, self._repr_balance())

    class Meta:
        verbose_name = 'colocataire'
        verbose_name_plural = 'colocataires'


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Roommate.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)
