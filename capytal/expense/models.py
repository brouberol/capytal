# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save, pre_delete

from category.models import Category
from roommate.models import Roommate


class Expense(models.Model):
    """The Expense class holds information about who spend what and when"""
    owner = models.ForeignKey(
        Roommate, related_name='expenses', verbose_name=u'émetteur')
    amount = models.FloatField(
        validators=[MinValueValidator(0)], verbose_name=u'montant')
    recipients = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='+',
        verbose_name=u'bénéficiaires')
    name = models.CharField(max_length=100, verbose_name=u'nom')
    date = models.DateTimeField()
    category =  models.ForeignKey(Category, related_name='+', verbose_name=u'catégorie')

    def __unicode__(self):
        return u'%s - %d€' % (self.name, self.amount)

    class Meta:
        verbose_name = u'dépense'
        verbose_name_plural = u'dépenses'


def increment_owner_balance(sender, instance, raw, using, **kwargs):
    """Increment the expense owner balance before the expense is saved
    for the first time or when the amount has been updated.

    """
    owner = instance.owner
    if instance.id:
        # Existing Expense has been modified
        old_expense = Expense.objects.get(id=instance.id)
        if old_expense.amount != instance.amount:
            owner.balance += (instance.amount - old_expense.amount)
            owner.save()
    else:
        # New Expense is saved to DB
        owner.balance += instance.amount
        owner.save()


def decrement_owner_balance(sender, instance, using, **kwargs):
    """Decrement the expense owner balance before the expense is deleted."""
    owner = instance.owner
    owner.balance -= instance.amount
    owner.save()


pre_save.connect(increment_owner_balance, sender=Expense)
pre_delete.connect(decrement_owner_balance, sender=Expense)
