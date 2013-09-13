# -*- coding: utf-8 -*-

from __future__ import division


from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save, pre_delete, m2m_changed

from category.models import Category
from roommate.models import Roommate
from .utils import balance_share


class Expense(models.Model):
    """The Expense class holds information about who spend what and when"""
    owner = models.ForeignKey(
        Roommate, related_name='expenses', verbose_name=u'émetteur')
    amount = models.FloatField(
        validators=[MinValueValidator(0)], verbose_name=u'montant')
    recipients = models.ManyToManyField(
        Roommate, related_name='+', verbose_name=u'bénéficiaires')
    name = models.CharField(max_length=100, verbose_name=u'nom')
    date = models.DateField()
    category =  models.ForeignKey(Category, related_name='+', verbose_name=u'catégorie')

    def __unicode__(self):
        return u'%s - %d€' % (self.name, self.amount)

    class Meta:
        verbose_name = u'dépense'
        verbose_name_plural = u'dépenses'


def pre_save_increment_owner_balance(sender, instance, raw, using, **kwargs):
    """Update the recipients expense balance after an expense amount
    is updated.

    """
    if instance.id:
        old = Expense.objects.get(id=instance.id)
        if old.amount != instance.amount:
            for recipient in instance.recipients.all():
                recipient.balance -= balance_share(
                    old, recipient, old.recipients.count())
                recipient.balance += balance_share(
                    instance, recipient, instance.recipients.count())
                recipient.save()
    else:
        instance.created = True


def m2m_changed_increment_owner_balance(sender, instance, action, reverse,
                                       model, pk_set, using, **kwargs):
    """Increment the expense recipients balance after it is created for the
    first time, updated or if some recipients are deleted.

    """
    # Recipients are added
    if action == 'post_add':
        # Newly created expense
        if hasattr(instance, 'created') and instance.created:
            for recipient in instance.recipients.all():
                recipient.balance += balance_share(
                    instance, recipient, instance.recipients.count())
                recipient.save()
            del instance.created

        # Existing expense with added recipients
        elif len(pk_set) != instance.recipients.count():
            old_recipients = [
                r for r in instance.recipients.all() if r.id not in pk_set]
            for recipient in instance.recipients.all():
                # The old recipients need to have their old balance canceled first
                if recipient in old_recipients:
                    recipient.balance -= balance_share(
                        instance, recipient, len(old_recipients))
                recipient.balance += balance_share(
                    instance, recipient, instance.recipients.count())
                recipient.save()

    # Recipients are deleted
    elif action == 'pre_remove':
        new_recipients = [
            r for r in instance.recipients.all() if r.id not in pk_set]
        for recipient in instance.recipients.all():
            recipient.balance -= balance_share(
                instance, recipient, instance.recipients.count())
            if recipient in new_recipients:
                recipient.balance += balance_share(
                    instance, recipient, len(new_recipients))
            recipient.save()


def pre_delete_decrement_owner_balance(sender, instance, using, **kwargs):
    """Decrement the expense recipients balance before the expense is deleted.

    """
    for recipient in instance.recipients.all():
        recipient.balance -= balance_share(
            instance, recipient, instance.recipients.count())
        recipient.save()


# Connect signals
pre_save.connect(
    pre_save_increment_owner_balance, sender=Expense)
pre_delete.connect(
    pre_delete_decrement_owner_balance, sender=Expense)
m2m_changed.connect(
    m2m_changed_increment_owner_balance, sender=Expense.recipients.through)
